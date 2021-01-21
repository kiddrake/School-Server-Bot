import discord
from discord.ext import commands

class admin_commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['delete'])
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Deleted ;)')

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} is unbanned!')
                return

def setup(client):
    client.add_cog(admin_commands(client))
