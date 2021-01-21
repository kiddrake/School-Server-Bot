import discord
from discord.ext import commands
import random

class Easteregg_functions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['Vape', 'vape'])
    async def vaping_is_epidemic_ettedgui(self, ctx):
        await ctx.send(file = discord.File('picture_vaping_is_an_epidemic.png'))

    @commands.command(aliases = ['Chad', 'chad'])
    async def walking_chad_ettedgui(self, ctx):
        await ctx.send(file = discord.File('picture_chad_ettedgui.png'))

    @commands.command(aliases = ['Ettedgui', 'ettedgui'])
    async def office_ettedgui(self, ctx):
        await ctx.send(file = discord.File('picture_office_ettedgui.png'))

    @commands.command(aliases = ['Schwimmer', 'schwimmer'])
    async def schwimmer_image(self, ctx):
        await ctx.send(file = discord.File('picture_schwimmer.png'))

    @commands.command(aliases = ['Nyancat', 'nyancat'])
    async def nyancat_gif(self, ctx):
        await ctx.send(file = discord.File('gif_nyancat.gif'))

    @commands.command(aliases = ['Wallach', 'wallach'])
    async def sad_wallach(self, ctx):
        await ctx.send(file = discord.File('picture_sad_wallach.png'))

    @commands.command(aliases = ['Zumwalt', 'zumwalt'])
    async def distorted_zumwalt(self, ctx):
        await ctx.send(file = discord.File('picture_distorted_zumwalt.png'))

    @commands.command(aliases = ["diaz", 'Diaz'])
    async def random_diaz_picture(self, ctx):
        picture_tag = random.randint(1,7)
        file_name = 'picture_diaz_' + str(picture_tag) + '.jpg'
        await ctx.send(file = discord.File(file_name))

    @commands.command(aliases = ['Pikachu', 'pikachu', 'PIKACHU', 'Emery', 'emery', 'EMERY'])
    async def emery_pikachu(self, ctx):
        await ctx.send(file = discord.File('picture_pikachu_emery.jpg'))

    @commands.command(aliases = ['Barr', 'barr', 'MsBarr', 'msbarr', 'KatieBarr', 'katiebarr'])
    async def office_barr(self, ctx):
        await ctx.send(file = discord.File('picture_barr.png'))

    @commands.command(aliases = ['Todoclaro', 'todoclaro', 'Allclear', 'allclear'])
    async def todo_claro_video(self, ctx):
        await ctx.send(file = discord.File('video_todo_claro_bell.mov'))

    @commands.command(aliases = ['Lui', 'lui', 'MsLui', 'Mslui', 'mslui'])
    async def normal_lui(self, ctx):
        await ctx.send(file = discord.File('picture_lui_flower_background.png'))

    @commands.command(aliases = ['Deakins', 'deakins', 'MrDeakins', 'Mrdeakins', 'mrdeakins'])
    async def staring_mr_deakins(self, ctx):
        await ctx.send(file = discord.File('picture_deakins_glaring.jpg'))

    @commands.command(aliases = ['Holz', 'holz'])
    async def long_face_holz(self, ctx):
        await ctx.send(file = discord.File('picture_holz_long.jpg'))

    @commands.command(aliases = ['Odonnell', "odonnell", "O'donell", "o'donnell"])
    async def zoomed_in_odonnell(self, ctx):
        await ctx.send(file = discord.File('picture_odonnell_zoomed_in.png'))

    @commands.command(aliases = ['Henry', 'henry'])
    async def staring_henry(self, ctx):
        await ctx.send(file = discord.File('picture_henry_blank_stare.jpg'))

    @commands.command(aliases = ["Bringedahl", 'bringedahl'])
    async def random_bringedahl_picture(self, ctx):
        picture_tag = random.randint(1,5)
        file_name = 'picture_bringedahl_' + str(picture_tag) + '.jpg'
        await ctx.send(file = discord.File(file_name))

    @commands.command(aliases = ["Jowers", 'jowers'])
    async def random_jowers_picture(self, ctx):
        picture_tag = random.randint(1,3)
        file_name = 'picture_jowers_' + str(picture_tag) + '.jpg'
        await ctx.send(file = discord.File(file_name))

def setup(client):
    client.add_cog(Easteregg_functions(client))
