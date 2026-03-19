from twitch_listener import TwitchListener
import command_parser
import input_emulator


def main():
    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║             CHAT PLAYS — Starting Up             ║")
    print("╠══════════════════════════════════════════════════╣")
    print(f"║  Valid commands : {sorted(command_parser.VALID_COMMANDS)}")
    print(f"║  Default hold   : {input_emulator.DEFAULT_KEY_HOLD_DURATION}s")
    print(f"║  Key mappings   :")
    for cmd, config_val in input_emulator.COMMANDS.items():
        if isinstance(config_val, dict):
            k = config_val.get("key")
            d = config_val.get("duration", input_emulator.DEFAULT_KEY_HOLD_DURATION)
        else:
            k = config_val
            d = input_emulator.DEFAULT_KEY_HOLD_DURATION
        print(f"║    {cmd:10s} → {k} ({d}s)")
    print("╠══════════════════════════════════════════════════╣")
    print("║  !start  — enable key presses                    ║")
    print("║  !stop   — pause key presses                     ║")
    print("║  Safety: move mouse to top-left corner to abort  ║")
    print("╚══════════════════════════════════════════════════╝")
    print()

    bot = TwitchListener()
    bot.run()


if __name__ == "__main__":
    main()
