# This module is responsible for filtering raw Twitch chat messages.
# It checks if a message is a valid game command and ignores everything else.

import json
import os

# Load the config file from the same folder as this script.
_config_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(_config_path, "r") as f:
    _config = json.load(f)

# Valid commands are the keys from the "commands" section in config.json.
# Change the config file to add/remove commands — no code changes needed.
VALID_COMMANDS = set(_config["commands"].keys())


def parse(raw_message: str) -> str | None:
    
    # Check if message is a valid command
    cleaned = raw_message.strip().lower()

    if cleaned in VALID_COMMANDS:
        return cleaned

    return None


# Quick self-test so you can run this file directly to verify it works.
if __name__ == "__main__":
    test_messages = [
        "jump",       # valid
        "  LEFT  ",   # valid (whitespace + uppercase)
        "ATTACK",     # valid (uppercase)
        "hello",      # invalid (not a command)
        "lol",        # invalid
        "jump now",   # invalid (extra words)
        "",           # invalid (empty)
        "up",         # valid
    ]

    print("=" * 40)
    print("  Command Parser — Self Test")
    print("=" * 40)

    for msg in test_messages:
        result = parse(msg)
        status = f"✔ '{result}'" if result else "✘ ignored"
        print(f"  Input: {msg!r:15s} → {status}")

    print()
    print(f"Valid commands: {sorted(VALID_COMMANDS)}")
