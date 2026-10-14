"""
Step 3: collect the question-answer pairs of a course into its unit files.

Reads the chapter texts that step 2 annotated with 'Frage:' / 'Antwort:' lines,
sorts every pair into a course unit and one of the three levels, and writes
courses/<id>/units/<unit>.generated.json - the format the application reads.

    python content_pipeline/03_collect_questions.py --course oop

The file it writes is overwritten on every run. Questions a teacher adds by
hand belong in a second file, conventionally <unit>.authored.json, which this
script never reads or touches; the manifest lists both and courselib merges
them. That is what makes it safe to re-run the pipeline on a course someone has
extended.

Which chapter belongs to which unit is declared per unit in the manifest:

    units:
      - id: ke1
        chapters:
          files: [KE1]        # chapter files named like this
          numbers_below: 6    # and numbered chapters below this

A numbered chapter goes to the first unit whose 'numbers_below' exceeds it; the
last unit takes the rest.
"""
import argparse
import glob
import json
import os
import re
import sys

from pathlib import Path

import yaml

REPOSITORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPOSITORY)

LEVEL_KEYS = ["REMEMBER", "APPLY", "ANALYZE"]
SKIPPED_CHAPTERS = {"Einsendeaufgaben"}


def level_of(question):
    """
    Sorts a question into one of the three levels by the way it is phrased.

    These are the rules of the published system, unchanged: asking what
    something is tests recall, asking how or why tests application, and asking
    for advantages, drawbacks or differences tests analysis.
    """
    if (question.startswith(("Was ist", "Was sind", "Was bedeutet", "Welche"))
            and not re.search("(Vorteil|Nachteil|Unterschied|Zweck|Grund|Beispiel)", question)):
        return 0
    if (question.startswith(("Wie", "Wann", "Warum", "Erklären"))
            or re.search("(Zweck|Grund|Beispiel)", question)):
        return 1
    return 2


def read_pairs(path):
    """
    Reads the question-answer pairs of one chapter file.

    The answer is the line following the question. The published version looked
    it up with lines.index(question), which returns the *first* occurrence and
    so paired a repeated question with the wrong answer; here the position is
    taken from the iteration itself.
    """
    with open(path, encoding="utf-8") as handle:
        lines = handle.readlines()

    pairs = []
    for index, line in enumerate(lines):
        if not line.startswith("Frage:"):
            continue
        if index + 1 >= len(lines):
            continue
        question = line.split(":", 1)[1].strip()
        answer = lines[index + 1]
        if not answer.startswith("Antwort:"):
            continue
        answer = answer.split(":", 1)[1].strip()
        if question and answer:
            pairs.append({"question": question, "answer": answer})
    return pairs


def unit_for(stem, units):
    """Returns the index of the unit a chapter file belongs to, or None."""
    for index, unit in enumerate(units):
        if stem in unit["files"]:
            return index

    try:
        number = float(stem)
    except ValueError:
        return None

    for index, unit in enumerate(units):
        if unit["numbers_below"] is not None and number < unit["numbers_below"]:
            return index
    return len(units) - 1


def read_units(manifest):
    """
    Reads the chapter mapping of every unit from the manifest.

    A unit that declares an empty block takes whatever is left over, which is
    how a course with a single unit is written.
    """
    units = []
    for raw in manifest["units"]:
        chapters = raw.get("chapters")
        units.append({
            "id": raw["id"],
            "declared": chapters is not None,
            "files": set((chapters or {}).get("files", [])),
            "numbers_below": (chapters or {}).get("numbers_below"),
        })
    return units


def collect(chapters_directory, units):
    """Sorts every pair of every chapter into (unit, level). Returns the pools."""
    pools = [[[] for _ in LEVEL_KEYS] for _ in units]
    unassigned = []

    for path in sorted(glob.glob(os.path.join(chapters_directory, "*.txt"))):
        stem = ".".join(Path(path).stem.split(".", 2)[:2])
        if stem in SKIPPED_CHAPTERS:
            continue
        index = unit_for(stem, units)
        if index is None:
            unassigned.append(stem)
            continue
        for pair in read_pairs(path):
            pools[index][level_of(pair["question"])].append(pair)

    return pools, unassigned


def drop_duplicates(pools):
    """
    Removes questions that occur more than once, across all units and levels.

    The published version popped from the list it was iterating over, which
    skips the element after each removal and let duplicates through.
    """
    seen = set()
    removed = 0
    for unit in pools:
        for level, questions in enumerate(unit):
            kept = []
            for pair in questions:
                if pair["question"] in seen:
                    removed += 1
                    continue
                seen.add(pair["question"])
                kept.append(pair)
            unit[level] = kept
    return removed


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-c", "--course", required=True, help="Id of the course to collect.")
    parser.add_argument("--chapters", help="Chapter directory, default: the manifest's source.")
    parser.add_argument("--output-dir", help="Where to write, default: the course's units/.")
    parser.add_argument("--suffix", default=".generated.json",
                        help="Suffix of the written files.")
    args = parser.parse_args()

    course_directory = os.path.join(REPOSITORY, "courses", args.course)
    manifest_path = os.path.join(course_directory, "manifest.yaml")
    if not os.path.isfile(manifest_path):
        sys.exit(f"No manifest at {manifest_path}")
    with open(manifest_path, encoding="utf-8") as handle:
        manifest = yaml.safe_load(handle)

    chapters = args.chapters
    if not chapters:
        source = manifest.get("source") or {}
        if "chapters" not in source:
            sys.exit("The manifest declares no source.chapters; pass --chapters.")
        chapters = os.path.join(course_directory, source["chapters"])
    if not os.path.isdir(chapters):
        sys.exit(f"No chapter directory at {chapters}")

    units = read_units(manifest)
    if not any(unit["declared"] for unit in units):
        sys.exit("No unit declares a 'chapters' block, so no chapter can be assigned. "
                 "Give at least one unit a 'chapters:' entry; an empty one means "
                 "'this unit takes every chapter'.")

    pools, unassigned = collect(chapters, units)
    removed = drop_duplicates(pools)

    output_directory = args.output_dir or os.path.join(course_directory, "units")
    os.makedirs(output_directory, exist_ok=True)

    print(f"{'unit':24} {'REMEMBER':>9} {'APPLY':>7} {'ANALYZE':>8}   file")
    total = 0
    for unit, levels in zip(units, pools):
        payload = {key: levels[index] for index, key in enumerate(LEVEL_KEYS)}
        name = f"{unit['id']}{args.suffix}"
        with open(os.path.join(output_directory, name), "w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        counts = [len(levels[i]) for i in range(len(LEVEL_KEYS))]
        total += sum(counts)
        print(f"{unit['id']:24} {counts[0]:9} {counts[1]:7} {counts[2]:8}   {name}")

    print(f"\n{total} questions written to {output_directory}")
    if removed:
        print(f"{removed} duplicate questions were dropped")
    if unassigned:
        print(f"Not assigned to any unit: {', '.join(sorted(set(unassigned))[:12])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
