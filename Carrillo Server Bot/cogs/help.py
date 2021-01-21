import discord
from discord.ext import commands

class help_command(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(colour = discord.Colour.orange())
        embed.set_author(name = 'Help')
        embed.add_field(name = '`Free-For-All Commands`', value = 'Below is a list of commands for everyone!', inline = False)
        embed.add_field(name = "`ping", value = 'Returns your ping value (internet speed in milliseconds)', inline = False)
        embed.add_field(name = "`8ball", value = 'Ask a True/False question!', inline = False)
        embed.add_field(name = "\`choose option_1 option_2 option_3 ...", value = "Can't decide on an option? Try using this!", inline = False)
        embed.add_field(name = "`no", value = 'NO', inline = False)
        embed.add_field(name = "`dog", value = "Hi, I'm Stopthat. Sometimes they call me 'Getbackhere'", inline = False)
        embed.add_field(name = "`cat", value = "Dogs have owners, cats have staff", inline = False)
        embed.add_field(name = "\`owo & \`uwu", value = 'For wholesome/cute vibes', inline = False)
        embed.add_field(name = "`pepsiman", value = 'Any Weather is Pepsi Weather', inline = False)
        embed.add_field(name = "`cokeman", value = "Pepsiman's greatest archenemy", inline = False)
        embed.add_field(name = "`nyancat", value = 'Nyan Cat!!!', inline = False)
        embed.add_field(name = '`f', value = 'Pay your respects', inline = False)
        embed.add_field(name = "`monke", value = 'Ooga ooga', inline = False)
        embed.add_field(name = "`yikes", value = 'Yikes...', inline = False)
        embed.add_field(name = "`bruh", value = 'The ultimate companion for "bruh moments"', inline = False)
        embed.add_field(name = '`Admin commands`', value = 'Below is a list of commands for the admins only', inline = False)
        embed.add_field(name = "\`clear # or \`delete #", value = 'Deletes # messages above', inline = False)
        embed.add_field(name = "\`kick, \`ban, \`unban", value = 'Self-explanatory...', inline = False)
        embed.add_field(name = '`Also...`', value = 'There are many hidden easteregg functions (more than miscellaneous ones, actually)! Try finding them!', inline = False)
        embed.add_field(name = 'Developer', value = 'Hyeonwoo (Drake) Wang', inline = False)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(help_command(client))
