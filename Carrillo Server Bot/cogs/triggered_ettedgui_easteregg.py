import discord
from discord.ext import commands

ettedgui_trigger_word = ['Vape', 'vape', 'VAPE', 'Vaping', 'vaping', 'VAPING', 'Juul', 'juul', 'JUUL', 'Bong', 'bong', 'BONG', 'V@pe', 'v@pe']

class ettedgui_easteregg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.content.startswith("`"):
            for trigger_word in ettedgui_trigger_word:
                if trigger_word in message.content:
                    if message.author != self.client.user:
                        await message.channel.send(file = discord.File('gif_ettedgui_triggered.gif'))
                        await message.channel.send(f"Confiscated! {message.author.mention}")

def setup(client):
    client.add_cog(ettedgui_easteregg(client))
