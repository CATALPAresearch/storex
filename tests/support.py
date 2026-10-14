"""
Shared helpers for the check scripts.

These are plain scripts rather than a pytest suite: most of them need the
running application, either inside the container (the ones that load models) or
over HTTP. Each prints one line per check and exits non-zero on failure.

    docker compose exec -T exam python -m tests.test_channel
    python tests/test_dialogue_http.py
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request

BASE = os.getenv("EXAM_URL", "http://localhost:5000")

_failures = []


def check(label, condition, detail=""):
    print(f"  [{'ok ' if condition else 'FAIL'}] {label}{(' - ' + str(detail)) if detail else ''}")
    if not condition:
        _failures.append(label)
    return bool(condition)


def finish():
    """Prints the verdict and exits. Call at the end of a check script."""
    print()
    if _failures:
        print(f"FAILURES ({len(_failures)}): " + ", ".join(_failures))
        sys.exit(1)
    print("all checks passed")
    sys.exit(0)


def require_free_slots():
    """
    Stops with a clear message when exams from an earlier run are still open.

    Without this the next check fails at exam creation and every later check
    cascades, which hides what actually went wrong.
    """
    status, health = call("GET", "/api/health")
    if status != 200:
        sys.exit(f"The application does not answer at {BASE} (http {status}).")
    if health.get("sessions"):
        sys.exit(f"{health['sessions']} exam(s) from an earlier run are still open. "
                 "Restart the service with 'docker compose restart exam'.")
    return health


def call(method, path, payload=None, timeout=120):
    """One JSON request against the running application."""
    data = json.dumps(payload).encode() if payload is not None else None
    request = urllib.request.Request(BASE + path, data=data, method=method,
                                     headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read()
            return response.status, (json.loads(body) if body else None)
    except urllib.error.HTTPError as error:
        body = error.read()
        return error.code, (json.loads(body) if body else None)


def drain(exam_id, since, want, limit=180):
    """
    Polls the event log until an event of a wanted type appears.

    :return: (events, since, state)
    """
    collected = []
    deadline = time.time() + limit
    state = "unknown"
    while time.time() < deadline:
        status, data = call("GET", f"/api/events?exam_id={exam_id}&since={since}")
        if status != 200:
            return collected, since, f"http {status}"
        since = data["since"]
        state = data["state"]
        collected.extend(data["events"])
        if any(event["type"] in want for event in collected) or data["closed"]:
            return collected, since, state
    return collected, since, "timeout"
