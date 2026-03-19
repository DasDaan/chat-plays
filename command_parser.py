import json
import os

_config_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(_config_path, "r") as f:
    _config = json.load(f)

VALID_COMMANDS = set(_config["commands"].keys())


def parse(raw_message: str) -> str | None:
    cleaned = raw_message.strip().lower()

    if cleaned in VALID_COMMANDS:
        return cleaned

    return None
