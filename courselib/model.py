"""
What a course is made of.

These objects are built once by courselib.loader and then shared by every exam
in the process, so they are immutable. Anything an exam mutates (the question
pools, which shrink as questions are asked) is copied by the QuestionManager.
"""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class OpenQuestion:
    """
    The broad question a course unit opens with.

    It has no sample answer; it is scored by the keywords alone, which is why
    the exam treats it differently from a predefined question (see
    ExamManager.get_evaluation, which branches on 'answer' in question).
    """
    question: str
    keywords: tuple = ()

    def as_dict(self):
        """The shape the exam expects a question in."""
        return {'question': self.question, 'keywords': list(self.keywords)}


@dataclass(frozen=True)
class Unit:
    """One course unit, with its questions grouped by level."""
    id: str
    title: str
    open_question: OpenQuestion | None = None
    # One tuple of questions per Level, in the order of the Level enum, so that
    # questions[Level.APPLY] works.
    questions: tuple = ()
    # Where they came from: (relative path, count) per file, in manifest order.
    # Generated and hand written questions live in separate files, see the
    # loader; this keeps track of how many each contributed.
    sources: tuple = ()

    @property
    def question_count(self):
        return sum(len(level) for level in self.questions)

    def levels_with_questions(self):
        """Names of the levels that actually hold questions."""
        from oral_exam.utils.helpers import Level
        return [level.name for level in Level if self.questions[level.value]]


@dataclass(frozen=True)
class Materials:
    """
    Optional material of a course.

    Every field may be absent; the exam then does without that capability
    rather than failing. See the README section on content integration.
    """
    # Technical terms, already parsed: a string, or a list of synonyms
    technical_terms: tuple = ()
    # Directory of the FAISS index used to find context for generated questions
    vector_store_path: str | None = None
    # The model the index was built with. A different one loads fine and
    # returns unrelated context, so the validator insists it is recorded.
    embedding_model: str | None = None
    # Course specific question generation model used to phrase hints
    paraphrase_model: str | None = None


@dataclass(frozen=True)
class Course:
    """A course the system can examine."""
    id: str
    title: str
    directory: str
    language: str = "de"
    description: str = ""
    units: tuple = ()
    materials: Materials = field(default_factory=Materials)
    # Resolved paths of the build-time inputs, see the manifest's source block.
    # The exam never uses these; the content pipeline does.
    source: dict = field(default_factory=dict)

    @property
    def unit_titles(self):
        return [unit.title for unit in self.units]

    @property
    def question_count(self):
        return sum(unit.question_count for unit in self.units)

    def summary(self):
        """One line for a listing."""
        return (f"{self.id}  {self.title}  "
                f"({len(self.units)} units, {self.question_count} questions)")
