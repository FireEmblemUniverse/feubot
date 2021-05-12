import discord
from discord.ext import commands
import os
import asyncio
import random


class Reactions(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Reactions Cog is online')

    @commands.command()
    async def brainblast(self, ctx):
        """Big Brain Explosion"""
        await ctx.send(file=discord.File("./Thunksplosion.gif"))

    @commands.command()
    async def ews(self, ctx):
        """disgusting list"""
        filenameslist = [os.path.splitext(f)[0] for f in os.listdir("./disgusting")]
        await ctx.send("```"+"\n".join(map(str, filenameslist))+"```")

    @commands.command()
    async def ew(self, ctx,*args):
        """disgusting"""
        requested = args
        ewlist = {a.lower(): a for a in os.listdir("./disgusting")}
        if len(requested) != 0:
            maxews = 5
            for request in requested:
                if maxews == 0: return
                else: maxews -= 1
                file_extension_or_not_pattern = re.compile('(\.[a-z]+)?$', re.I | re.M)
                found = False
                for extension in ['.png', '.jpg', '.gif', '.jpeg']:
                    request_file = file_extension_or_not_pattern.sub(extension, request).lower()
                    if request_file in ewlist:
                        found = True
                        await ctx.send(file=discord.File("./disgusting/"+ewlist[request_file]))
                if not found:
                    await ctx.send("Use >>ews to see a list of accepted names.")
        else:
            await ctx.send(file=discord.File("./disgusting/"+random.choice([a for a in ewlist.values()])))

    @commands.command()
    async def bonk(self, ctx):
        "No Horny"
        bonklist = {a.lower(): a for a in os.listdir("./bonk")}
        await ctx.send(file=discord.File("./bonk/"+random.choice([a for a in bonklist.values()])))

    @commands.command(aliases=["incredible"])
    async def fuckingincredible(self, ctx):###
        """fuckingincredible.png"""
        await ctx.send("http://i.imgur.com/yt4hXhJ.png")

    @commands.command()
    async def crackers(self, ctx):
        """jumping boat monkeys!"""###
        await ctx.send(file=discord.File("./Holy_crackers.png"))

    @commands.command()
    async def hector(self, ctx):
        """judges you"""
        await ctx.send(file=discord.File("./hectorpc.png"))

    @commands.command()
    async def eliwood(self, ctx):
        """:("""
        await ctx.send(file=discord.File("./eliwoodpc.jpg"))

    @commands.command()
    async def lyn(self, ctx):
        """>:("""
        await ctx.send(file=discord.File("./lynpc.png"))

    @commands.command()
    async def spritans(self, ctx):
        """REEE"""
        await ctx.send("muh")
        await asyncio.sleep(1)
        await ctx.send("SPRITANS")
        await asyncio.sleep(2)
        await ctx.send("***REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE***")


    @commands.command(aliases=["reeee", 'ree'])
    async def reee(self, ctx):
        """REEEEEEEEEEEEEEEEEEE"""
        action = random.choice([1,2])
        if action==1:
            msg = "*REEE*"
            await asyncio.sleep(0.5)
            await asyncio.sleep(0.25)
            await ctx.send(msg + "                   **REEEEEEEEEEE**                  ")
            await asyncio.sleep(0.5)
            await ctx.send("***REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE***")
        else:
            await ctx.send(file=discord.File("./reee.gif"))

    @commands.command(aliases=["f", 'respects'])
    async def F(self, ctx):
        """Press F to pay respects."""
        await ctx.send(file=discord.File("./respects.jpeg"))

    @commands.command()
    async def enough(self, ctx):
        """you wouldn't like me when i'm angry"""
        await ctx.send(file=discord.File("./enough.png"))

    @commands.command()
    async def creepy(self, ctx):
        """stay away"""
        await ctx.send(file=discord.File("./creepy.png"))

    @commands.command()
    async def tethys(self, ctx):
        """dancer think"""
        await ctx.send(file=discord.File("./tethys.png"))

    @commands.command()
    async def marisa(self, ctx):
        """u srs"""
        await ctx.send(file=discord.File("./marisa.png"))

    @commands.command()
    async def lel(self, ctx):
        """lel"""
        img=random.choice(["./lel.png","./lel2.png"])
        await ctx.send(file=discord.File(img))

    @commands.command(pass_context=True, hidden=True)
    async def approve(self, ctx):
        pid = str(ctx.message.author.id)
        if pid == "171863408822452224":
            await ctx.send(file=discord.File('./approved.png'))
        elif pid == '59462571601702912':
            await ctx.send(file=discord.File('./Letha_Seal_of_Approval.png'))
        else:
            await ctx.send(file=discord.File('./FEU_Seal.png'))

    @commands.command(aliases=["OK"])
    async def ok(self, ctx):
        """ok"""
        await ctx.send(file=discord.File("./ok.png"))

    @commands.command()
    async def uberthink(self, ctx):
        """ðŸ¤”"""
        await ctx.send(file=discord.File("./uberthink.gif"))

    @commands.command(aliases=["awfuldisplay"])
    async def awful(self, ctx):
        """for when someone posts cringe"""
        await ctx.send(file=discord.File("./awful.jpg"))
    
def setup(bot):
    bot.add_cog(Reactions(bot))
