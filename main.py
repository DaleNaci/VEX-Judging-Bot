import os

from dotenv import load_dotenv
from discord import Intents, Client, Message


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)


@client.event
async def on_ready():
    print("Ready")


@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return
    
    await send_message(message, message.content)



async def send_message(message: Message, user_message: str) -> None:
    if user_message.lower() == "hello":
        await message.channel.send("Hello, world!")


client.run(TOKEN)