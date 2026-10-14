"""
Locations the dialogue system writes to.

Test transcripts used to be written into the repository tree. In a container
that tree is read-only in practice, so everything generated goes into one
directory which docker compose mounts from the host.
"""
import os

REPO_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def output_directory():
    """Returns the directory for generated transcripts, creating it if needed."""
    directory = os.getenv("OUTPUT_DIR") or os.path.join(REPO_DIRECTORY, "output")
    os.makedirs(directory, exist_ok=True)
    return directory


def output_file(name):
    """Returns a path inside the output directory."""
    return os.path.join(output_directory(), name)
