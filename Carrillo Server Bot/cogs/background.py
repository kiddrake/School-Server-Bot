import discord
from discord.ext import commands

class background_managements(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.new_students_channel = self.client.get_channel(742482129056956507)
        await self.new_students_channel.send(f'{member.mention} is here! Please make sure to check the puma emoji below the rules to access the rest of the server.\nMy command prefix is "\`".\nIf you need any help with using me, please use "\`help" or ask the admins!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        self.new_students_channel = self.client.get_channel(742482129056956507)
        await self.new_students_channel.send(f'{member.mention} Bye Bye... :(')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please input all required values for the command UwU')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid command :(')

def setup(client):
    client.add_cog(background_managements(client))
