"""
Locations the dialogue system writes to.

Everything produced by a run - exam transcripts, component reports - goes into
one directory, which docker compose mounts from the host. It holds throwaway
results, not content: course material lives in courses/<id>/ and the published
evaluation of the paper in docs/evaluation/.
"""
import os

# oral_exam/utils/paths.py -> the repository root
REPO_DIRECTORY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_directory():
    """Returns the directory for run output, creating it if needed."""
    directory = os.getenv("RUNS_DIR") or os.path.join(REPO_DIRECTORY, "runs")
    os.makedirs(directory, exist_ok=True)
    return directory


def run_file(name, course_id=None):
    """
    Returns a path inside the run directory.

    :param course_id: prefixed to the name, so that a throwaway result stays
        attributable to the course it came from.
    """
    if course_id:
        name = f"{course_id}_{name}"
    return os.path.join(run_directory(), name)
