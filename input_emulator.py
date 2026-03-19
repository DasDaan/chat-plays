import json
import os
import time
import pydirectinput

pydirectinput.FAILSAFE = True

_config_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(_config_path, "r") as f:
    _config = json.load(f)

DEFAULT_KEY_HOLD_DURATION = _config.get("key_hold_duration", 0.1)
COMMANDS = _config.get("commands", {})


def execute(command: str) -> bool:
    cmd_data = COMMANDS.get(command)

    if cmd_data is None:
        return False

    if isinstance(cmd_data, dict):
        key = cmd_data.get("key")
        duration = cmd_data.get("duration", DEFAULT_KEY_HOLD_DURATION)
    else:
        key = cmd_data
        duration = DEFAULT_KEY_HOLD_DURATION

    if not key:
        return False

    pydirectinput.keyDown(key)
    time.sleep(duration)
    pydirectinput.keyUp(key)

    return True
