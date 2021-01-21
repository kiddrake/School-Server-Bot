import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
import random

client = commands.Bot(command_prefix = "`")
client.remove_command('help')

@client.event
async def on_ready():
    status_message.start()
    print("All Good :)")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

status = cycle(['Netflix', 'The Amazing World of Gumball', "Little Einsteins", "My Little Pony", "Regular Show", "Zumwalt's Showme Lectures", "Adventure Time", "Youtube", 'We Bare Bears', "Pornhub", "Zoom Lectures", "Rick and Morty", "The Mandalorian"])

@tasks.loop(minutes = 5)
async def status_message():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = next(status)))

client.run('NzQyNDcwNzcwMjgxNjc2ODcy.XzGlyg.7CpO6ILusDaOHp2-wpB1FPLhphI')
