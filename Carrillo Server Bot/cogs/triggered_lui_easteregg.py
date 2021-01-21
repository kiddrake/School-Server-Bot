import discord
from discord.ext import commands

lui_trigger_word = ['Cheat', 'cheat', 'CHEAT', 'Copy', 'copy', 'COPY']

class lui_easteregg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.content.startswith("`"):
            for trigger_word in lui_trigger_word:
                if trigger_word in message.content:
                    if message.author != self.client.user:
                        await message.channel.send(file = discord.File('picture_lui_academic_honesty.jpg'))

def setup(client):
    client.add_cog(lui_easteregg(client))
