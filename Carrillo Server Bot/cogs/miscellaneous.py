import discord
from discord.ext import commands
import random
import requests

class Miscallaneous(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['Definitely',
                     'Cloudy...',
                     'Maybe...idk',
                     'Hah. Funny joke lol',
                     'Nope',
                     '100% yes']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(aliases = ['choice', 'choose'])
    async def choose_random(self, ctx, *args):
        answer = random.choice(args)
        await ctx.send(f'I choose: {answer}')

    @commands.command(aliases = ["Monke", 'monke', 'Monkey', 'monkey'])
    async def random_picture_monke(self, ctx):
        picture_tag = random.randint(1,6)
        file_name = 'picture_monke_' + str(picture_tag) + '.jpg'
        await ctx.send(file = discord.File(file_name))

    @commands.command(aliases = ['No', 'no', 'NO'])
    async def tee_ko_no(self, ctx):
        await ctx.send(file = discord.File('picture_no_tee_ko.png'))

    @commands.command(aliases = ['Bruh', 'bruh', 'BRUH'])
    async def bruh_picture(self, ctx):
        await ctx.send(file = discord.File('picture_bruh.png'))

    @commands.command(aliases = ['Yikes', 'yikes', 'YIKES'])
    async def yikes_can_picture(self, ctx):
        await ctx.send(file = discord.File('picture_yikes.jpg'))

    @commands.command(aliases = ['F', 'f'])
    async def pay_your_respect(self, ctx):
        await ctx.send(file = discord.File('picture_press_f_to_pay_respects.jpg'))
        await ctx.send(f'{ctx.message.author.mention} has paid his/her respects')

    @commands.command(aliases = ['Pepsi', 'pepsi', 'Pepsiman', 'pepsiman'])
    async def pepsiman_picture(self, ctx):
        await ctx.send(file = discord.File('picture_pepsi_man.jpg'))

    @commands.command(aliases = ['Owo', 'owo', 'oWo', 'OwO'])
    async def owo_picture(self, ctx):
        await ctx.send(file = discord.File('picture_owo.png'))

    @commands.command(aliases = ['Uwu', 'uwu', 'uWu', 'UwU'])
    async def uwu_picture(self, ctx):
        await ctx.send(file = discord.File('picture_uwu.png'))

    @commands.command(aliases = ['Coke', 'coke', 'Cokeman', 'cokeman', 'Cocacola', 'cocacola'])
    async def coke_man_picture(self, ctx):
        await ctx.send(file = discord.File('picture_cokeman.png'))

    @commands.command(aliases = ['Dog', 'DOG'])
    async def dog(self, ctx):
        raw_data = requests.get('https://dog.ceo/api/breeds/image/random')
        await ctx.send(raw_data.json()['message'])

    @commands.command(aliases = ['Cat', 'CAT'])
    async def cat(self, ctx):
        api_key_authentication = requests.get('https://thecatapi.com/v1/images?api_key=bf9840b1-bff3-463a-b862-bde38905b221')
        raw_data = requests.get('https://api.thecatapi.com/v1/images/search')
        await ctx.send(raw_data.json()[0]["url"])


def setup(client):
    client.add_cog(Miscallaneous(client))
