import os
from dotenv import load_dotenv
from twitchio.ext import commands
import command_parser

# load_dotenv() reads the .env file in the same folder and makes the values
# available through os.getenv(). This keeps your token OUT of the code.
load_dotenv()

TWITCH_TOKEN   = os.getenv("TWITCH_TOKEN")
TWITCH_CHANNEL = os.getenv("TWITCH_CHANNEL")

# We create a class that inherits from twitchio's commands.Bot.
class TwitchListener(commands.Bot):

    def __init__(self):
        # Initialize the bot with our token and the channel to join.
        # prefix="!" means the bot will also recognize !commands (like !hello).
        # We don't use commands yet, but it's nice to have ready.
        super().__init__(
            token=TWITCH_TOKEN,
            prefix="!",
            initial_channels=[TWITCH_CHANNEL],
        )

    # Connect the bot to twitch
    async def event_ready(self):
        """Called once the bot has successfully connected to Twitch."""
        print("=" * 50)
        print(f"  Bot is online!")
        print(f"  Logged in as : {self.nick}")
        print(f"  Listening to : {TWITCH_CHANNEL}")
        print("=" * 50)
        print()

    # Chat message arrives
    async def event_message(self, message):
        # Ignore messages sent by the bot itself to avoid loops.
        if message.echo:
            return

        # Run the message through our command parser.
        cmd = command_parser.parse(message.content)

        if cmd:
            # Valid command — highlight it so it stands out in the console.
            print(f"  ► [COMMAND] {message.author.name} → {cmd}")
        else:
            # Regular chat — still print it, but less prominently.
            print(f"    [{message.author.name}]: {message.content}")


# Entry point / Start up
if __name__ == "__main__":
    bot = TwitchListener()
    bot.run()
