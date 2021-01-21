import discord
from discord.ext import commands

zumwalt_trigger_word = ['Phone', 'phone', 'PHONE']

class zumwalt_easteregg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.content.startswith("`"):
            for trigger_word in zumwalt_trigger_word:
                if trigger_word in message.content:
                    if message.author != self.client.user:
                        await message.channel.send(file = discord.File('picture_zumwalt.jpg'))

def setup(client):
    client.add_cog(zumwalt_easteregg(client))
