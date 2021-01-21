import discord
from discord.ext import commands

emery_trigger_word = ['Pikachu', 'pikachu', 'PIKACHU', 'Pichu', 'pichu', 'PICHU']

class emery_pikachu_easteregg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.content.startswith("`"):
            for trigger_word in emery_trigger_word:
                if trigger_word in message.content:
                    if message.author != self.client.user:
                        await message.channel.send(file = discord.File('picture_pikachu_emery.jpg'))

def setup(client):
    client.add_cog(emery_pikachu_easteregg(client))
