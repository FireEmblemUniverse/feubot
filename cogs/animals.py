import discord
import os
import random
from discord.ext import commands

class Animals(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Animals Cog is online')

    @commands.command()
    async def cat(self, ctx, *args):
        catlist = os.listdir("./cats")
        await ctx.send(file=discord.File("./cats/"+random.choice(catlist)))

    @commands.command()
    async def dog(self, ctx, *args):
        doglist = os.listdir("./dogs")
        await ctx.send(file=discord.File("./dogs/"+random.choice(doglist)))

    @commands.command()
    async def bunny(self, ctx, *args):
        bunlist = os.listdir("./bunnies")
        await ctx.send(file=discord.File("./bunnies/"+random.choice(bunlist)))

    @commands.command()
    async def animal(self, ctx, *args):
        anilist = os.listdir("./animals")
        await ctx.send(file=discord.File("./animals/"+random.choice(anilist)))
        
def setup(bot):
    bot.add_cog(Animals(bot))
