import discord
from discord.ext import commands
import os
import random


class Helpful(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Helpful Cog is online')

    @commands.command()
    async def report7z(self, ctx):
        """Report7z reminder"""
        await ctx.send("Please send report7z.")
        await ctx.send("https://dw.ngmansion.xyz/doku.php?id=en:guide:febuildergba:report7z")

    @commands.command()
    async def howtomod(self, ctx):
        """Gives information on how to use the !mod command."""
        await ctx.send("First, have Developer Mode enabled (Settings -> Appearance -> Developer Mode).")
        await ctx.send("Then, click the `...` by the offending message, and click \"Copy Link\".")
        await ctx.send("Then simple say !mod <n> <link>, where <n> is the rule it violates, and <link> is the pasted link to the message.")
        await ctx.send("If you do not have Developer Mode, you may instead of a link, write a short description of where the infraction took place, and by who.")
        await ctx.send("Note that after requesting moderation, the message requesting moderation will be removed.")


    @commands.command()
    async def goldmine(self, ctx):
        """everything you ever wanted"""
        embed=discord.Embed(title="Unified FE Hacking Dropbox", url='https://www.dropbox.com/sh/xl73trcck2la799/AAAMdpNSGQWEzYkLEQEiEhGFa?dl=0', description="All the hacking resources you could ever need, in one place", color=0xefba01)
        # embed.set_thumbnail(url='http://i.imgur.com/Bg5NSga.png')
        await ctx.send(embed=embed)


    @commands.command(aliases=["repo"])
    async def repository(self, ctx):
        """graphics for you"""
        embed=discord.Embed(title="Emblem Anims", url='https://emblem-anims.herokuapp.com/', description="Get your animations here (credits missing on some, check just in case!)", color=0x4286f4)
        await ctx.send(embed=embed)

    @commands.command()
    async def mugs(self, ctx):
        """Link to image of all GBAFE mugs."""
        await ctx.send("http://doc.feuniverse.us/static/resources/mugs.png")

    @commands.command()
    async def hit(self, ctx, number, type="2RN"):
        """Convert 2RN/fates hit to actual chance"""
        try:
            num = int(number)
        except ValueError:
            await ctx.send("Specify an integer 0-100")
            return
        if (num < 0) or (num > 100):
            await ctx.send("Specify an integer 0-100")
            return
        if type.upper()=="2RN":
            table = [0.00, 0.03, 0.10, 0.21, 0.36, 0.55, 0.78, 1.05, 1.36, 1.71, 2.10, 2.53, 3.00, 3.51, 4.06, 4.65, 5.28, 5.95, 6.66, 7.41, 8.20, 9.03, 9.90, 10.81, 11.76, 12.75, 13.78, 14.85, 15.96, 17.11, 18.30, 19.53, 20.80, 22.11, 23.46, 24.85, 26.28, 27.75, 29.26, 30.81, 32.40, 34.03, 35.70, 37.41, 39.16, 40.95, 42.78, 44.65, 46.56, 48.51, 50.50, 52.47, 54.40, 56.29, 58.14, 59.95, 61.72, 63.45, 65.14, 66.79, 68.40, 69.97, 71.50, 72.99, 74.44, 75.85, 77.22, 78.55, 79.84, 81.09, 82.30, 83.47, 84.60, 85.69, 86.74, 87.75, 88.72, 89.65, 90.54, 91.39, 92.20, 92.97, 93.70, 94.39, 95.04, 95.65, 96.22, 96.75, 97.24, 97.69, 98.10, 98.47, 98.80, 99.09, 99.34, 99.55, 99.72, 99.85, 99.94, 99.99, 100.00]
        elif type.upper()=="FATES":
            table = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50.5,51.83,53.17,54.5,55.83,57.17,58.5,59.83,61.17,62.5,63.83,65.17,66.5,67.83,69.17,70.5,71.83,73.17,74.5,75.83,77.17,78.5,79.83,81.17,82.5,83.83,85.12,86.35,87.53,88.66,89.73,90.75,91.72,92.63,93.49,94.3,95.05,95.75,96.4,96.99,97.53,98.02,98.45,98.83,99.16,99.43,99.65,99.82,99.93,99.99,100]
        else:
            await ctx.send("Valid types are 2RN, Fates")
            return
        await ctx.send(str(table[num]))

    @commands.command()
    async def roll(self, ctx, number, type="2RN"):
        """rolls hit or miss (e.g. >>hit 50 1rn/2rn[default]/fates)"""
        try:
            num = int(number)
        except ValueError:
            await ctx.send("Specify an integer 0-100")
            return
        if (num < 0) or (num > 100):
            await ctx.send("Specify an integer 0-100")
            return
        if type.upper()=="1RN":
            rolled = random.randint(1,100)
        elif type.upper()=="2RN":
            rolled = (random.randint(1,100) + random.randint(1,100))>>1
        elif type.upper()=="FATES":
            rolled = random.randint(1,100)
            if rolled > 50:
                rolled = ((rolled*3) + random.randint(1,100))>>2
        else:
            await ctx.send("Valid types are 1RN, 2RN, Fates")
            return
        if rolled <= num: await ctx.send("HIT (%d)" % rolled)
        else: await ctx.send("MISS (%d)" % rolled)

    @commands.command(name="diceroll")
    async def rollDie(self, ctx, n : int):
        if n <= 0:
            await ctx.send("Specify a positive integer.")
            return
        res = random.randrange(n) + 1
        await ctx.send(str(res))
    
def setup(bot):
    bot.add_cog(Helpful(bot))
