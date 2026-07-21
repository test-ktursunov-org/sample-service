import json
import sys
import time


def log_request(method: str, path: str, status: int, started_at: float) -> None:
    record = {
        "method": method,
        "path": path,
        "status": status,
        "duration_ms": round((time.monotonic() - started_at) * 1000, 2),
    }
    sys.stdout.write(json.dumps(record) + "\n")
