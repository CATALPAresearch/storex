"""
Reads course content from disk.

A course is a directory holding a manifest.yaml and the question files it
refers to. Everything is read once into the immutable objects of
courselib.model, so no file is touched while an exam is running.

The loader collects problems instead of raising on the first one, so that
`python -m courselib.validate` can report everything a content author got
wrong in one go.
"""
import json
import logging
import os
import re
import threading

import yaml

from oral_exam.utils.helpers import Level
from oral_exam.utils.preprocessing import load_terms

from courselib.model import Course, Materials, OpenQuestion, Unit

logger = logging.getLogger(__name__)

MANIFEST_NAME = "manifest.yaml"
# The JSON keys a unit file may use, in the order of the Level enum
LEVEL_KEYS = [level.name for level in Level]
ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_-]*$")

MANIFEST_KEYS = {"id", "title", "language", "description", "units", "materials", "source"}
# "chapters" is read by the content pipeline, not by the application
UNIT_KEYS = {"id", "title", "questions", "levels", "open_question", "chapters"}
MATERIAL_KEYS = {"technical_terms", "vector_store", "paraphrase_model"}
QUESTION_KEYS = {"question", "answer", "keywords"}

_registry = {}
_problems = {}
_loaded = False
_lock = threading.RLock()


class CourseError(Exception):
    """A course could not be loaded. Carries every problem found."""
    def __init__(self, course_id, problems):
        self.course_id = course_id
        self.problems = problems
        super().__init__(f"Course '{course_id}': " + "; ".join(problems))


class UnknownCourse(KeyError):
    """No course with that id is available."""


def content_root():
    """Directory the courses live in."""
    override = os.getenv("COURSES_DIR")
    if override:
        return override
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "courses")


def discover(root=None):
    """Returns the course directories under root, sorted by name."""
    root = root or content_root()
    if not os.path.isdir(root):
        return []
    directories = []
    for name in sorted(os.listdir(root)):
        if name.startswith((".", "_")):
            continue
        directory = os.path.join(root, name)
        if os.path.isfile(os.path.join(directory, MANIFEST_NAME)):
            directories.append(directory)
    return directories


class _Reader:
    """Reads one course directory, collecting problems as it goes."""

    def __init__(self, directory):
        self.directory = os.path.abspath(directory)
        self.course_id = os.path.basename(self.directory)
        self.problems = []
        self.warnings = []

    def fail(self, message):
        self.problems.append(message)

    def warn(self, message):
        self.warnings.append(message)

    def resolve(self, relative, label):
        """
        Resolves a path inside the course directory.
        Returns None if it is missing or points outside the course.
        """
        if not isinstance(relative, str) or not relative.strip():
            self.fail(f"{label}: no path given")
            return None
        path = os.path.realpath(os.path.join(self.directory, relative))
        if not path.startswith(os.path.realpath(self.directory) + os.sep):
            self.fail(f"{label}: '{relative}' points outside the course directory")
            return None
        if not os.path.exists(path):
            self.fail(f"{label}: '{relative}' does not exist")
            return None
        return path

    # --- manifest ---------------------------------------------------------
    def read_manifest(self):
        path = os.path.join(self.directory, MANIFEST_NAME)
        try:
            with open(path, encoding="utf-8") as handle:
                manifest = yaml.safe_load(handle)
        except (OSError, yaml.YAMLError) as error:
            self.fail(f"{MANIFEST_NAME} cannot be read: {error}")
            return None
        if not isinstance(manifest, dict):
            self.fail(f"{MANIFEST_NAME} must contain a mapping")
            return None
        for key in set(manifest) - MANIFEST_KEYS:
            self.warn(f"unknown manifest entry '{key}'")
        return manifest

    def read_identity(self, manifest):
        course_id = manifest.get("id")
        if not isinstance(course_id, str) or not course_id:
            self.fail("id is missing")
        elif not ID_PATTERN.match(course_id):
            self.fail(f"id '{course_id}' may only hold lower case letters, digits, '-' and '_'")
        elif course_id != self.course_id:
            self.fail(f"id '{course_id}' does not match the directory name '{self.course_id}'")

        title = manifest.get("title")
        if not isinstance(title, str) or not title.strip():
            self.fail("title is missing")

        language = manifest.get("language", "de")
        if language != "de":
            # Prompts, feedback wording and the keyword matching are all German
            self.warn(f"language '{language}': the dialogue and the keyword matching are German")
        return course_id, title, language

    # --- units ------------------------------------------------------------
    def read_question_file(self, path, label):
        """Reads one question file into a tuple of lists, ordered like Level."""
        try:
            with open(path, encoding="utf-8") as handle:
                payload = json.load(handle)
        except (OSError, ValueError) as error:
            self.fail(f"{label}: cannot be read ({error})")
            return None
        if not isinstance(payload, dict):
            self.fail(f"{label}: must contain an object keyed by level")
            return None

        unknown = set(payload) - set(LEVEL_KEYS)
        if unknown:
            self.fail(f"{label}: unknown level(s) {sorted(unknown)}, allowed are {LEVEL_KEYS}")
            return None

        levels = []
        for key in LEVEL_KEYS:
            entries = payload.get(key, [])
            if not isinstance(entries, list):
                self.fail(f"{label}: '{key}' must be a list")
                return None
            for index, entry in enumerate(entries):
                if not isinstance(entry, dict):
                    self.fail(f"{label}: {key}[{index}] must be an object")
                    return None
                for field_name in ("question", "answer"):
                    value = entry.get(field_name)
                    if not isinstance(value, str) or not value.strip():
                        self.fail(f"{label}: {key}[{index}] has no {field_name}")
                        return None
                for key_name in set(entry) - QUESTION_KEYS:
                    self.warn(f"{label}: {key}[{index}] has an unknown entry '{key_name}'")
            levels.append(entries)
        return tuple(levels)

    def read_questions(self, entry, label):
        """
        Reads the question files of one unit and merges them level by level.

        A unit may name a single file or several. Several is what lets a course
        keep generated and hand written questions apart: the content pipeline
        overwrites its own file on every run and never touches the others, so a
        teacher can add questions without fearing the next pipeline run. The
        merged questions compete equally when one is drawn.

        :return: (questions, sources) or (None, []) if a file could not be read.
        """
        entries = entry if isinstance(entry, list) else [entry]
        if not entries:
            self.fail(f"{label}: questions is empty")
            return None, []

        merged = [[] for _ in LEVEL_KEYS]
        sources = []
        for relative in entries:
            path = self.resolve(relative, f"{label}: questions")
            if path is None:
                return None, []
            levels = self.read_question_file(path, f"{label} ({relative})")
            if levels is None:
                return None, []
            for index, level in enumerate(levels):
                merged[index].extend(level)
            sources.append((relative, sum(len(level) for level in levels)))

        return tuple(tuple(level) for level in merged), sources

    def read_open_question(self, raw, label):
        if raw is None:
            return None
        if not isinstance(raw, dict):
            self.fail(f"{label}: open_question must be a mapping")
            return None
        question = raw.get("question")
        if not isinstance(question, str) or not question.strip():
            self.fail(f"{label}: open_question has no question")
            return None
        keywords = raw.get("keywords", [])
        if not isinstance(keywords, list) or not all(isinstance(word, str) for word in keywords):
            self.fail(f"{label}: open_question keywords must be a list of strings")
            return None
        return OpenQuestion(question=question, keywords=tuple(keywords))

    def read_units(self, manifest):
        raw_units = manifest.get("units")
        if not isinstance(raw_units, list) or not raw_units:
            self.fail("units is missing or empty")
            return ()

        units = []
        seen = set()
        for position, raw in enumerate(raw_units):
            label = f"unit {position + 1}"
            if not isinstance(raw, dict):
                self.fail(f"{label}: must be a mapping")
                continue
            for key in set(raw) - UNIT_KEYS:
                self.warn(f"{label}: unknown entry '{key}'")

            unit_id = raw.get("id")
            if not isinstance(unit_id, str) or not unit_id.strip():
                self.fail(f"{label}: id is missing")
                continue
            label = f"unit '{unit_id}'"
            if unit_id in seen:
                self.fail(f"{label}: id is used twice")
                continue
            seen.add(unit_id)

            title = raw.get("title")
            if not isinstance(title, str) or not title.strip():
                self.fail(f"{label}: title is missing")
                continue

            questions, sources = self.read_questions(raw.get("questions"), label)
            if questions is None:
                continue

            unit = Unit(id=unit_id, title=title,
                        open_question=self.read_open_question(raw.get("open_question"), label),
                        questions=questions, sources=tuple(sources))

            declared = raw.get("levels")
            if declared is not None:
                if not isinstance(declared, list):
                    self.fail(f"{label}: levels must be a list")
                else:
                    actual = unit.levels_with_questions()
                    if sorted(declared) != sorted(actual):
                        self.fail(f"{label}: declares levels {sorted(declared)} "
                                  f"but holds questions for {actual}")
            units.append(unit)
        return tuple(units)

    # --- materials --------------------------------------------------------
    def read_materials(self, manifest):
        raw = manifest.get("materials")
        if raw is None:
            return Materials()
        if not isinstance(raw, dict):
            self.fail("materials must be a mapping")
            return Materials()
        for key in set(raw) - MATERIAL_KEYS:
            self.warn(f"materials: unknown entry '{key}'")

        terms = ()
        if "technical_terms" in raw:
            path = self.resolve(raw["technical_terms"], "materials: technical_terms")
            if path:
                try:
                    terms = load_terms(path)
                except OSError as error:
                    self.fail(f"materials: technical_terms cannot be read ({error})")

        store_path = None
        embedding_model = None
        store = raw.get("vector_store")
        if store is not None:
            if not isinstance(store, dict):
                self.fail("materials: vector_store must be a mapping")
            else:
                store_path = self.resolve(store.get("path"), "materials: vector_store.path")
                if store_path:
                    missing = [name for name in ("index.faiss", "index.pkl")
                               if not os.path.isfile(os.path.join(store_path, name))]
                    if missing:
                        self.fail(f"materials: vector_store is missing {missing}")
                        store_path = None
                embedding_model = store.get("embedding_model")
                if not isinstance(embedding_model, str) or not embedding_model.strip():
                    # A FAISS index built with another encoder loads happily and
                    # returns unrelated context, so this cannot be optional
                    self.fail("materials: vector_store.embedding_model is missing")

        paraphrase_model = raw.get("paraphrase_model")
        if paraphrase_model is not None and (not isinstance(paraphrase_model, str)
                                             or not paraphrase_model.strip()):
            self.fail("materials: paraphrase_model must be a model name")
            paraphrase_model = None

        return Materials(technical_terms=terms,
                         vector_store_path=store_path,
                         embedding_model=embedding_model,
                         paraphrase_model=paraphrase_model)

    def read_source(self, manifest):
        """
        Reads the optional source block, which records what the course was
        built from. Only the content pipeline uses it.

        A missing source path is **not** an error: the build material is
        deliberately left out of the container image, where only units/ and
        materials/ are needed. Reporting it as a problem would make every
        course unloadable in production.
        """
        raw = manifest.get("source")
        if raw is None:
            return {}
        if not isinstance(raw, dict):
            self.fail("source must be a mapping")
            return {}

        resolved = {}
        for key, relative in raw.items():
            if not isinstance(relative, str) or not relative.strip():
                self.fail(f"source: {key} has no path")
                continue
            path = os.path.realpath(os.path.join(self.directory, relative))
            if not path.startswith(os.path.realpath(self.directory) + os.sep):
                self.fail(f"source: {key} points outside the course directory")
                continue
            resolved[key] = path
            if not os.path.exists(path):
                self.warn(f"source: {key} '{relative}' is not present "
                          "(expected when the build material is not deployed)")
        return resolved

    def read(self):
        manifest = self.read_manifest()
        if manifest is None:
            return None
        course_id, title, language = self.read_identity(manifest)
        units = self.read_units(manifest)
        materials = self.read_materials(manifest)
        source = self.read_source(manifest)

        if units and not any(unit.question_count for unit in units):
            self.fail("the course holds no questions at all")
        if self.problems:
            return None

        return Course(id=course_id, title=title, directory=self.directory,
                      language=language, description=manifest.get("description", "") or "",
                      units=units, materials=materials, source=source)


def load_course(directory):
    """
    Loads one course directory.

    :raises CourseError: with every problem found.
    """
    reader = _Reader(directory)
    course = reader.read()
    if course is None:
        raise CourseError(reader.course_id, reader.problems)
    return course


def inspect_course(directory):
    """Reads a course and returns (course_or_None, problems, warnings)."""
    reader = _Reader(directory)
    course = reader.read()
    return course, reader.problems, reader.warnings


def load_all(force=False, root=None):
    """
    Loads every course that can be found. A broken course is skipped and its
    problems are kept in errors(); it never makes the application unusable.
    """
    global _loaded
    with _lock:
        if _loaded and not force:
            return _registry
        _registry.clear()
        _problems.clear()
        for directory in discover(root):
            try:
                course = load_course(directory)
            except CourseError as error:
                _problems[error.course_id] = error.problems
                logger.error("Course '%s' was skipped: %s", error.course_id,
                             "; ".join(error.problems))
                continue
            _registry[course.id] = course
            logger.info("Loaded course %s", course.summary())
        _loaded = True
        return _registry


def all_courses():
    """Loadable courses, the default first, then by title."""
    load_all()
    default = default_course_id()
    return sorted(_registry.values(), key=lambda course: (course.id != default, course.title))


def get(course_id):
    """Returns one course by id."""
    load_all()
    if course_id not in _registry:
        raise UnknownCourse(course_id)
    return _registry[course_id]


def default_course_id():
    """DEFAULT_COURSE if it is loadable, otherwise the first course by id."""
    load_all()
    preferred = os.getenv("DEFAULT_COURSE")
    if preferred and preferred in _registry:
        return preferred
    return next(iter(sorted(_registry)), None)


def errors():
    """Problems of the courses that could not be loaded, keyed by id."""
    load_all()
    return dict(_problems)
