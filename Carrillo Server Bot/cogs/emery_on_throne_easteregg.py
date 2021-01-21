import discord
from discord.ext import commands

king_emery_trigger_word = ['Emperor', 'emperor', 'EMPEROR', 'Prince', 'prince', 'PRINCE', 'Majesty', 'majesty', 'MAJESTY']

class king_emery_easteregg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.content.startswith("`"):
            for trigger_word in king_emery_trigger_word:
                if trigger_word in message.content:
                    if message.author != self.client.user:
                        await message.channel.send(file = discord.File('picture_emery_on_throne.jpg'))

def setup(client):
    client.add_cog(king_emery_easteregg(client))
