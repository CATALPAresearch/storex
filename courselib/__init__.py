"""
Course content: the questions, materials and structure the exam works on.

Content lives in courses/<id>/ and holds no code; this package reads it.
"""
from courselib.loader import (
    CourseError,
    UnknownCourse,
    all_courses,
    content_root,
    default_course_id,
    discover,
    errors,
    get,
    inspect_course,
    load_all,
    load_course,
)
from courselib.model import Course, Materials, OpenQuestion, Unit

__all__ = [
    "Course", "CourseError", "Materials", "OpenQuestion", "Unit", "UnknownCourse",
    "all_courses", "content_root", "default_course_id", "discover", "errors",
    "get", "inspect_course", "load_all", "load_course",
]
