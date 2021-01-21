import discord
from discord.ext import commands

ettedgui_trigger_word = ['Vape', 'vape', 'VAPE', 'Vaping', 'vaping', 'VAPING', 'Juul', 'juul', 'JUUL', 'Bong', 'bong', 'BONG', 'V@pe', 'v@pe']

class ettedgui_vape_counter(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.counter = 0

    @commands.Cog.listener()
    async def on_message(self, message):
        self.ettedgui_office = self.client.get_channel(743375787079499827)
        if not message.content.startswith("`"):
            for trigger_word in ettedgui_trigger_word:
                if trigger_word in message.content:
                    if message.author != self.client.user:
                        self.counter += 1
                        await self.ettedgui_office.send(f"Someone got caught vaping! {self.counter} juuls collected so far")
                    else:
                        return

def setup(client):
    client.add_cog(ettedgui_vape_counter(client))
