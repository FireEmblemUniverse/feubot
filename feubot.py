import discord
from discord.ext import commands
import asyncio
import re
import random
import os

import useful, memes, reactions

bot = commands.Bot(command_prefix=['!', '>>', 'feubot '], description='this is feubot.')

# bot = commands.Bot(command_prefix=['##', 'feubeta '], description='this is feubot beta.')

#Set up in reverse order so that useful displays first, etc.

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="Reading the doc!"))

@bot.command()
async def donate():
    """you know it"""
    await bot.say("https://donorbox.org/donate-to-circles")

token = os.environ.get('TOKEN', default=None)
if token is None:
    token = open('./token').read().replace('\n','')

reactions.setup(bot)
memes.setup(bot)
useful.setup(bot)

bot.run(token)
