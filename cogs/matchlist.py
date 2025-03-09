import discord
from discord.ext import commands

from api.robotevents.api_handler import get_match_list


class MatchList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.content.lower() == "matchlist":
            await message.channel.send(get_match_list(58565))


    @commands.command()
    async def matchlist(self, ctx):
        match_list_json = get_match_list(58565)
        first_match_json = match_list_json["data"][0]

        await ctx.send(first_match_json)

    
async def setup(bot):
    await bot.add_cog(MatchList(bot))