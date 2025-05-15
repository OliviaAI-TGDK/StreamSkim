import json, time, os
from pathlib import Path

VECTOR_PATH = Path.home() / ".bluepill_vector.json"

def watch_vector_file():
    last_mtime = None
    print("[Trace Viewer] Watching for telemetry vector updates...")

    while True:
        if VECTOR_PATH.exists():
            mtime = VECTOR_PATH.stat().st_mtime
            if mtime != last_mtime:
                last_mtime = mtime
                with open(VECTOR_PATH) as f:
                    data = json.load(f)
                    print("\n=== [Telemetry Vector Update] ===")
                    for k, v in data.items():
                        print(f"{k.upper():>12}: {v}")
        time.sleep(2)

if __name__ == "__main__":
    watch_vector_file()