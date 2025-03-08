import discord
from discord.ext import commands


class HelloWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        
        if message.content.lower() == "hello":
            await message.channel.send("Hello, world!")


async def setup(bot):
    await bot.add_cog(HelloWorld(bot))