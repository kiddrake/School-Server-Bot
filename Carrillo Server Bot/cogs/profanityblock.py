import discord
from discord.ext import commands
import re
import discord.utils

profanity_list = ['nigger', 'fgt', 'nigga', 'nibba', 'dyke', 'coon', 'koon', 'tranny', 'chink', 'gook', 'wetback', 'zipperhead', 'kike', 'kyke', 'faggot', 'nickgur', 'iggern', 'fag', 'beaner', 'redskin', 'ragehead', 'gringo']

punc_list = [",", "?", "!", ":", ";", "-", "_", "—", '"', ".", '“', '”', "%", "'"]

def charlist(word):
    return [q for q in word]

def remove(sample,a):
    char_list = []
    for char in charlist(sample):
        if char != a:
            char_list.append(char)
    return "".join(char_list)

def textcleaner(textchunk, punctuation_list):
    word_list = textchunk.split()
    for word in word_list:
        new_word = word
        for punctuation in punctuation_list:
            new_word = remove(new_word, punctuation)
        word_list[word_list.index(word)] = new_word
    return "".join(word_list)

def all_lowercase(text):
    for f in re.findall("[A-Z]", text):
        text = text.replace(f, f.lower())
    return text

def remove_numbers(text):
    for f in re.findall("\d", text):
        text = text.replace(f, "")
    return text

def number_to_alphabet(text):
    for f in re.findall("0", text):
        text = text.replace(f, "o")
    for f in re.findall("3", text):
        text = text.replace(f, "e")
    for f in re.findall("4", text):
        text = text.replace(f, "a")
    for f in re.findall("5", text):
        text = text.replace(f, "s")
    for f in re.findall("1", text):
        text = text.replace(f, "i")
    for f in re.findall("@", text):
        text = text.replace(f, "a")
    return text

class profanity_block(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.content.startswith("`"):
            return
        original = message.content
        joined_chunk = textcleaner(original, punc_list)
        with_numbers = all_lowercase(joined_chunk)
        suspended_role = discord.utils.get(message.author.guild.roles, id = 743372204695093268)
        for profanity_word in profanity_list:
            if profanity_word in remove_numbers(with_numbers):
                await message.channel.purge(limit = 1)
                await message.channel.send(f"Please keep the chat clean, {message.author.mention}")
                await message.author.add_roles(suspended_role)
                return
            if profanity_word in number_to_alphabet(with_numbers):
                await message.channel.purge(limit = 1)
                await message.channel.send(f"Please keep the chat clean, {message.author.mention}")
                await message.author.add_roles(suspended_role)
                return


def setup(client):
    client.add_cog(profanity_block(client))
