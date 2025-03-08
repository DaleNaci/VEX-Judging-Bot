import discord
from discord.ext import commands


class MatchList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        
        pass


    
async def setup(bot):
    await bot.add_cog(MatchList(bot))