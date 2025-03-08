import discord


class JudgingBot(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
    

    async def on_ready(self):
        print(f"Logged in as {self.user}")
    
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        
        if message.content.lower() == "hello":
            await message.channel.send("Hello, world!")