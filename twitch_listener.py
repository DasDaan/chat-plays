import os
from dotenv import load_dotenv
from twitchio.ext import commands
import command_parser
import input_emulator

load_dotenv()

TWITCH_TOKEN   = os.getenv("TWITCH_TOKEN")
TWITCH_CHANNEL = os.getenv("TWITCH_CHANNEL")


class TwitchListener(commands.Bot):

    def __init__(self):
        super().__init__(
            token=TWITCH_TOKEN,
            prefix="!",
            initial_channels=[TWITCH_CHANNEL],
        )
        self.input_enabled = True

    async def event_ready(self):
        print("=" * 50)
        print(f"  Bot is online!")
        print(f"  Logged in as : {self.nick}")
        print(f"  Listening to : {TWITCH_CHANNEL}")
        print(f"  Input enabled: {self.input_enabled}")
        print("=" * 50)
        print()

    async def event_message(self, message):
        if message.echo:
            return

        await self.handle_commands(message)

        cmd = command_parser.parse(message.content)

        if cmd:
            if self.input_enabled:
                input_emulator.execute(cmd)
                print(f"  ► [PRESS] {message.author.name} → {cmd}")
            else:
                print(f"  ⏸ [PAUSED] {message.author.name} → {cmd}")
        else:
            print(f"    [{message.author.name}]: {message.content}")

    @commands.command(name="start")
    async def cmd_start(self, ctx):
        self.input_enabled = True
        print("  ✔ Input ENABLED")
        await ctx.send("Inputs are now ON!")

    @commands.command(name="stop")
    async def cmd_stop(self, ctx):
        self.input_enabled = False
        print("  ⏸ Input DISABLED")
        await ctx.send("Inputs are now OFF!")
