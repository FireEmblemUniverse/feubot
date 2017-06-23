import discord
from discord.ext import commands as bot
import os, random, re

class Memes:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def whois(self,*args):
        """roy is our boy"""
        if len(args) > 0:
            lord = ' '.join(args)
            if (lord.lower() in ['circles','circleseverywhere']):
                await self.bot.say(lord + " is my dad")
                return
            elif (lord.lower() == 'feditor'):
                await self.bot.say("`" + lord + " a shit`")
                return
            elif lord[0].lower() in 'bcdfghjklmnpqrstvwxz':
                blord = 'b'+lord[1:]
            else:
                blord = 'b'+lord
            await self.bot.say(lord + " is our " + blord)

    @bot.command()
    async def reply(self):
        """r e p l y s o o n"""
        await self.bot.say("reply :soon: :smile:")

    @bot.command()
    async def goofs(self):
        """list goofs"""
        filenameslist = [os.path.splitext(f)[0] for f in os.listdir("./goofs")]
        await self.bot.say("```"+"\n".join(map(str, filenameslist))+"```")

    @bot.command()
    async def goof(self,*args):
        """show goof"""
        requested = args
        gooflist = {a.lower(): a for a in os.listdir("./goofs")}
        if len(requested) != 0:
            maxgoofs = 5
            for request in requested:
                if maxgoofs == 0: return
                else: maxgoofs -= 1
                file_extension_or_not_pattern = re.compile('(\.[a-z]+)?$', re.I | re.M)
                found = False
                for extension in ['.png', '.jpg', '.gif', '.jpeg']:
                    request_file = file_extension_or_not_pattern.sub(extension, request).lower()
                    if request_file in gooflist:
                        found = True
                        await self.bot.upload("./goofs/"+gooflist[request_file])
                if not found:
                    await self.bot.say("Use >>goofs to see a list of accepted goofs.")
        else:
            await self.bot.upload("./goofs/"+random.choice([a for a in gooflist.values()]))

    @bot.command()
    async def fury(self):
    """2 FAST 2 FURYOUS"""
    await self.bot.say("Don't you mean `>>erin`?")

    @bot.command()
    async def erin(self):
        """ERIN INTENSIFIES"""
        await self.bot.upload("./erinyous.gif")

    @bot.command()
    async def ea(self):
        """EVERYTHING ASSEMBLER"""
        everythingassemblerstring = """``` _____                 _   _   _
|   __|_ _ ___ ___ _ _| |_| |_|_|___ ___
|   __| | | -_|  _| | |  _|   | |   | . |
|_____|\_/|___|_| |_  |_| |_|_|_|_|_|_  |
                  |___|             |___|
 _____                   _   _
|  _  |___ ___ ___ _____| |_| |___ ___
|     |_ -|_ -| -_|     | . | | -_|  _|
|__|__|___|___|___|_|_|_|___|_|___|_|```"""
        await self.bot.say(everythingassemblerstring)

    @bot.command()
    async def doot(self):
        """doot doot"""
        flip = random.choice([0,1])
        if flip ==1:
            await self.bot.say("""<:doot:324593825815461889> <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> <:doot:324593825815461889> <:doot:324593825815461889>
<:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
<:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
<:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
<:doot:324593825815461889> <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:""")
        else:
            await self.bot.upload("./DOOT.png")

    @bot.command()
    async def createwaifu(self,*args):
        """:wink:"""
        heads = [
            "<:zigludo:252132877678936064>",
            "<:zahlman:230166256412655616>",
            "<:narcian:271805925017387008>",
            "<:marf:230171669635923968>",
            "<:lloydwut:313590046978605059>",
            "<:linde:325036388833558539>",
            "<:lilina:230156179916062720>",
            "<:kent:232283653642780672>",
            "<:kaga:293121861905022976>",
            "<:ick:280744571640610816>",
            "<:florina:230904896067469312>",
            "<:FEU:230151584846184448>",
            "<:fa:303774076252454912>",
            "<:elise:235616193065517066>",
            "<:eliwood:232283812938121217>",
            "<:elbert:232283825974149120>",
            "<:EAmoe:317182514559188994>",
            "<:doot:324593825815461889>",
            "<:donate:230166446146191362>",
            "<:doc:280527122802540544>",
            "<:colorz:230159530158194688>",
            "<:circles:238177111418863617>",
            "<:celica:272027128231362571>",
            "<:BBQ:230169373694885888>",
            "<:arch_mini:230160993299202068>",
            "<:cam_thumb:307559627573428224>",
            "<:dat:292422389197701121>",
            "<:thighs:294965155819683840>"]
        if len(args) > 0: head = ' '.join(args)
        else: head = random.choice(heads)
        await self.bot.say(head + """
<:personality:274564774979960832>
<:thighs:294965155819683840>""")

    @bot.command()
    async def casual(self):
        """just play phoenix"""
        barflist = os.listdir("./casual")
        await self.bot.upload("./casual/"+random.choice(barflist))

    @bot.command()
    async def arch(self):
    """do something with arch"""
    direction = random.choice([":arrow_down:", ":arrow_up:"])
    await self.bot.say(direction+" with <:arch_mini:230160993299202068>")


def setup(bot):
    bot.add_cog(Memes(bot))
