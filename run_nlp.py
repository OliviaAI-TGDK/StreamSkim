# run_nlp.py
import os
import json

print("[Bluepill Listener] Activated. Monitoring telemetry vectors...")

telemetry_path = "/data/data/com.termux/files/home/.bluepill_vector.json"

try:
    with open(telemetry_path, "r") as f:
        data = json.load(f)
        print("[run_nlp] Beacon:", data.get("beacon", "N/A"))
        print("[run_nlp] Interface:", data.get("interface", "unknown"))
        print("[run_nlp] Q-Vector:", data.get("q_vector", ""))
        # Simulate call to NLP modules
        os.system("echo '[run_nlp] Processing through OliviaAI NLP...'")
except Exception as e:
    print("[run_nlp] Error reading telemetry:", e)