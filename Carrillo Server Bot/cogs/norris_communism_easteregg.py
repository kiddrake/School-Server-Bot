import discord
from discord.ext import commands

communism_trigger_word = ['Communism', 'communism', 'COMMUNISM', 'Soviet', 'soviet', 'SOVIET']

class communism_easteregg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.content.startswith("`"):
            for trigger_word in communism_trigger_word:
                if trigger_word in message.content:
                    if message.author != self.client.user:
                        await message.channel.send(file = discord.File('picture_norris_communism.jpg'))

def setup(client):
    client.add_cog(communism_easteregg(client))
