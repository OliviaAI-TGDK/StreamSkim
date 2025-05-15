-- bluepill_monitor.lua
-- Continuously executes Bluepill.sh on interval, with fallback detection
-- Copyright TGDK. All rights reserved.

local os = require("os")
local io = require("io")

-- === Configuration ===
local interval = 30        -- Seconds between executions
local bluepill_path = "./Bluepill.sh"
local logfile = "/data/data/com.termux/files/home/.bluepill_loop.log"

-- === Logger Function ===
local function log(msg)
    local file = io.open(logfile, "a")
    if file then
        file:write(os.date("[%Y-%m-%d %H:%M:%S] ") .. msg .. "\n")
        file:close()
    end
end

-- === Daemon Loop ===
log("Bluepill Monitor activated.")
while true do
    log("Executing Bluepill.sh...")
    local result = os.execute(bluepill_path)
    if result == 0 then
        log("Bluepill.sh executed successfully.")
    else
        log("ERROR: Bluepill.sh failed with code " .. tostring(result))
    end

    -- Wait before next run
    os.execute("sleep " .. interval)
end