import json
import os
import time
import pydirectinput

pydirectinput.FAILSAFE = True

_config_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(_config_path, "r") as f:
    _config = json.load(f)

KEY_HOLD_DURATION = _config.get("key_hold_duration", 0.1)
COMMAND_TO_KEY = _config["commands"]


def execute(command: str) -> bool:
    key = COMMAND_TO_KEY.get(command)

    if key is None:
        return False

    pydirectinput.keyDown(key)
    time.sleep(KEY_HOLD_DURATION)
    pydirectinput.keyUp(key)

    return True
