import os

from dotenv import load_dotenv
import discord

from bot import JudgingBot


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = JudgingBot(intents=intents)
bot.run(TOKEN)