from twitch_listener import TwitchListener
import command_parser
import input_emulator


def main():
    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║             CHAT PLAYS — Starting Up            ║")
    print("╠══════════════════════════════════════════════════╣")
    print(f"║  Valid commands : {sorted(command_parser.VALID_COMMANDS)}")
    print(f"║  Key hold time  : {input_emulator.KEY_HOLD_DURATION}s")
    print(f"║  Key mappings   :")
    for cmd, key in input_emulator.COMMAND_TO_KEY.items():
        print(f"║    {cmd:10s} → {key}")
    print("╠══════════════════════════════════════════════════╣")
    print("║  !start  — enable key presses                   ║")
    print("║  !stop   — pause key presses                    ║")
    print("║  Safety: move mouse to top-left corner to abort  ║")
    print("╚══════════════════════════════════════════════════╝")
    print()

    bot = TwitchListener()
    bot.run()


if __name__ == "__main__":
    main()
