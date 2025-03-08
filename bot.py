import os

import discord
from discord.ext import commands


class JudgingBot(commands.Bot):
    def __init__(self, *, command_prefix: str, intents: discord.Intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
    

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                cog_name = f"cogs.{filename[:-3]}"

                await self.load_extension(cog_name)


    async def on_ready(self):
        print(f"Logged in as {self.user}")