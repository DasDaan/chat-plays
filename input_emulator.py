# This module translates valid game commands into actual key presses
# using pydirectinput (DirectX scancodes that work in most games).

import json
import os
import time
import pydirectinput

# Safety: pydirectinput has a failsafe — move your mouse to the top-left
# corner of the screen to instantly abort the program.
pydirectinput.FAILSAFE = True

# Load settings and key mappings from config.json.
_config_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(_config_path, "r") as f:
    _config = json.load(f)

KEY_HOLD_DURATION = _config.get("key_hold_duration", 0.1)
COMMAND_TO_KEY = _config["commands"]


def execute(command: str) -> bool:
    """Press the key mapped to the given command.

    Holds the key down for KEY_HOLD_DURATION seconds, then releases it.
    Returns True if the key was pressed, False if the command has no mapping.
    """
    key = COMMAND_TO_KEY.get(command)

    if key is None:
        print(f"  ⚠ No key mapping for command: {command!r}")
        return False

    # Hold the key for a short duration so games actually register it.
    pydirectinput.keyDown(key)
    time.sleep(KEY_HOLD_DURATION)
    pydirectinput.keyUp(key)

    return True


# Self-test: press each mapped key one by one with a visible delay.
# Open a text editor like Notepad FIRST, then run this script to see the output.
if __name__ == "__main__":
    print("=" * 50)
    print("  Input Emulator — Self Test")
    print("  Open Notepad and click inside it NOW!")
    print("  Keys will start pressing in 3 seconds...")
    print("=" * 50)

    time.sleep(3)

    test_commands = ["up", "down", "left", "right", "jump", "attack"]

    for cmd in test_commands:
        print(f"  Pressing: {cmd!r} → key '{COMMAND_TO_KEY[cmd]}'")
        execute(cmd)
        time.sleep(0.5)  # pause between presses so you can see each one

    print()
    print("Done! Check your Notepad for the typed keys.")
