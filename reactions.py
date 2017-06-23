import discord
from discord.ext import commands as bot
import os, random, re, asyncio

class Reactions:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def spritans(self):
        """REEE"""
        await self.bot.say("muh")
        await asyncio.sleep(1)
        await self.bot.say("SPRITANS")
        await asyncio.sleep(2)
        await self.bot.say("***REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE***")

    @bot.command()
    async def hector(self):
        """judges you"""
        await self.bot.upload("./hectorpc.png")

    @bot.command()
    async def fuckingincredible(self):
    """fuckingincredible.png"""
    await self.bot.say("http://i.imgur.com/yt4hXhJ.png")

    @bot.command()
    async def ews(self):
        """disgusting list"""
        filenameslist = [os.path.splitext(f)[0] for f in os.listdir("./disgusting")]
        await self.bot.say("```"+"\n".join(map(str, filenameslist))+"```")

    @bot.command()
    async def ew(self,*args):
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
                        await self.bot.upload("./disgusting/"+ewlist[request_file])
                if not found:
                    await self.bot.say("Use >>ews to see a list of accepted names.")
        else:
            await self.bot.upload("./disgusting/"+random.choice([a for a in ewlist.values()]))

    @bot.command()
    async def crackers(self):
        """jumping boat monkeys!"""
        await self.bot.upload("./Holy_crackers.png")


def setup(bot):
    bot.add_cog(Reactions(bot))
