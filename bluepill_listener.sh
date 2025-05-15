#!/bin/bash

# bluepill_listener.sh
# TGDK Quantum Telemetry Listener Node
# Copyright TGDK. All rights reserved.

TELEMETRY_FILE="/tmp/bluepill_vector.json"
INTERPLEX_POST="http://localhost:8080/gentuo-valhalla-interplex/telemetry"
LOG_FILE="/var/log/tgdk/bluepill_listener.log"

mkdir -p "$(dirname "$LOG_FILE")"

echo "[Bluepill Listener] Activated. Monitoring telemetry vectors..."

# Watch for new telemetry packets
inotifywait -m -e modify "$TELEMETRY_FILE" --format '%w%f' |
while read file; do
    echo "[Bluepill Listener] Change detected in $file"

    TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    PAYLOAD=$(cat "$file")

    echo "[Bluepill Listener] [$TIMESTAMP] Forwarding telemetry..."
    RESPONSE=$(curl -s -X POST "$INTERPLEX_POST" -H "Content-Type: application/json" --data "$PAYLOAD")

    echo "[Bluepill Listener] [$TIMESTAMP] Response: $RESPONSE" >> "$LOG_FILE"
    echo "[Bluepill Listener] Logged response and cycled."
done