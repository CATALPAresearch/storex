"""
Shared helper for the pipeline steps: find a course and its source material.

The steps are scripts, not modules, so they import this by path rather than as
part of a package.
"""
import os
import sys

import yaml

REPOSITORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def course_directory(course_id):
    directory = os.path.join(REPOSITORY, "courses", course_id)
    if not os.path.isfile(os.path.join(directory, "manifest.yaml")):
        sys.exit(f"No course '{course_id}' under {os.path.join(REPOSITORY, 'courses')}")
    return directory


def read_manifest(course_id):
    with open(os.path.join(course_directory(course_id), "manifest.yaml"), encoding="utf-8") as f:
        return yaml.safe_load(f)


def source_path(course_id, key, override=None, required=True):
    """
    Resolves one entry of the manifest's source block, for example 'chapters'.

    :param override: a path given on the command line, which wins.
    """
    if override:
        return override
    source = read_manifest(course_id).get("source") or {}
    if key not in source:
        if not required:
            return None
        sys.exit(f"The manifest of '{course_id}' declares no source.{key}; pass it explicitly.")
    return os.path.join(course_directory(course_id), source[key])


def materials_path(course_id, key, override=None):
    """Resolves one entry of the manifest's materials block."""
    if override:
        return override
    materials = read_manifest(course_id).get("materials") or {}
    value = materials.get(key)
    if isinstance(value, dict):
        value = value.get("path")
    if not value:
        return None
    return os.path.join(course_directory(course_id), value)
