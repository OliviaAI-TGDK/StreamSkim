
#!/data/data/com.termux/files/usr/bin/bash
# Bluepill Telemetry Watcher – OliviaAI Auto-Executor
echo "[Bluepill Listener] Activated. Monitoring telemetry vectors..."

TELEMETRY_PATH="/data/data/com.termux/files/home/.bluepill_vector.json"
WATCHDIR="$(dirname "$TELEMETRY_PATH")"
FILENAME="$(basename "$TELEMETRY_PATH")"

inotifywait -m -e close_write --format "%w%f" "$WATCHDIR" 2>/dev/null | while read FILE
do
    if [[ "$FILE" == "$TELEMETRY_PATH" ]]; then
        echo "[Bluepill Listener] New vector detected. Launching OliviaAI StreamSkim..."
        python run_nlp.py
    fi
done