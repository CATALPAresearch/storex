"""
Checks course content against what the exam expects.

    python -m courselib.validate                 every course
    python -m courselib.validate --course oop    one course
    python -m courselib.validate --strict        warnings count as failures
    python -m courselib.validate --json          machine readable

It reads manifests and question files only; no model weights are downloaded,
so it runs in well under a second. Whether the models named in a manifest can
actually be fetched is warmup's business, not the validator's.
"""
import argparse
import json
import os
import sys

from courselib.loader import content_root, discover, inspect_course


def check_embedding_model(course, warnings):
    """
    The vector store must record the encoder it was built with.

    An index built with another model loads without complaint and returns
    unrelated context for every generated question, so a mismatch is reported
    here or nowhere.
    """
    declared = course.materials.embedding_model
    if not declared:
        return []
    try:
        from oral_exam import models
    except ImportError as error:  # pragma: no cover - only if the app is not installed
        warnings.append(f"cannot compare the embedding model ({error})")
        return []
    if declared != models.EMBEDDING_MODEL:
        return [f"materials: vector_store was built with '{declared}', "
                f"but the application embeds with '{models.EMBEDDING_MODEL}'"]
    return []


def inspect(directory):
    """Returns a result dict for one course directory."""
    course, problems, warnings = inspect_course(directory)
    result = {
        "id": os.path.basename(os.path.abspath(directory)),
        "directory": directory,
        "problems": list(problems),
        "warnings": list(warnings),
    }
    if course is not None:
        result["problems"].extend(check_embedding_model(course, result["warnings"]))
        result["title"] = course.title
        result["units"] = len(course.units)
        result["questions"] = course.question_count
        result["terms"] = len(course.materials.technical_terms)
        # Per unit, how many questions each file contributed. A teacher adding
        # an *.authored.json file sees here whether it was picked up.
        result["units_detail"] = [{
            "id": unit.id,
            "questions": unit.question_count,
            "sources": [{"file": name, "questions": count} for name, count in unit.sources],
        } for unit in course.units]
        result["vector_store"] = course.materials.vector_store_path is not None
        result["paraphrase_model"] = course.materials.paraphrase_model
    result["ok"] = not result["problems"]
    return result


def describe_units(result):
    """One line per unit, listing where its questions came from."""
    lines = []
    for unit in result.get("units_detail", []):
        if len(unit["sources"]) > 1:
            origin = ", ".join(f"{s['questions']} from {s['file']}" for s in unit["sources"])
        else:
            origin = unit["sources"][0]["file"] if unit["sources"] else "-"
        lines.append(f"        {unit['id']:24} {unit['questions']:5} questions  ({origin})")
    return lines


def describe(result):
    """The one line summary of a course."""
    if not result["ok"]:
        return f"FAIL  {result['id']}"
    parts = [f"{result['units']} units", f"{result['questions']} questions"]
    if result["terms"]:
        parts.append(f"{result['terms']} technical terms")
    if result["vector_store"]:
        parts.append("vector store")
    if result["paraphrase_model"]:
        parts.append("own paraphrase model")
    return f"OK    {result['id']}  {result.get('title', '')}  ({', '.join(parts)})"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate course content.")
    parser.add_argument("--course", help="Validate only this course id.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="Print the report as JSON.")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="List every unit and where its questions came from.")
    parser.add_argument("--root", help="Directory holding the courses.")
    args = parser.parse_args(argv)

    root = args.root or content_root()
    directories = discover(root)
    if args.course:
        directories = [d for d in directories if os.path.basename(d) == args.course]
        if not directories:
            print(f"No course '{args.course}' in {root}", file=sys.stderr)
            return 2
    if not directories:
        print(f"No courses found in {root}", file=sys.stderr)
        return 2

    results = [inspect(directory) for directory in directories]

    if args.as_json:
        print(json.dumps({"root": root, "courses": results}, ensure_ascii=False, indent=2))
    else:
        print(f"Courses in {root}:")
        for result in results:
            print(describe(result))
            if args.verbose:
                for line in describe_units(result):
                    print(line)
            for problem in result["problems"]:
                print(f"        error:   {problem}")
            for warning in result["warnings"]:
                print(f"        warning: {warning}")

    failed = [r for r in results if not r["ok"]]
    warned = [r for r in results if r["warnings"]]
    if failed:
        return 1
    if args.strict and warned:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
