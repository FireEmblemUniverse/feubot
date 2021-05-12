import discord
import random
import os
from sys import argv
from dotenv import load_dotenv
import asyncio
import urllib
import urllib.request
import urllib.error
import sys, traceback
import re
import json
from discord.ext import commands


class Memes(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Memes Cog is online')

    @commands.command()
    async def heckbeard (self, ctx):
        """Hector's true calling"""
        await ctx.send(file=discord.File("./heckbeard.png"))

    @commands.command()
    async def gotodead (self, ctx):
        """Kirby's not messing around any more."""
        await ctx.send(file=discord.File("./gotodead.png"))

    @commands.command()
    async def familyfriendly (self, ctx):
        """Pooh the berserker"""
        await ctx.send(file=discord.File("./familyfriendly.png"))
    
    @commands.command()
    async def cattheft (self, ctx):
        """gimme"""
        await ctx.send("It’s not really theft. It’s unsolicited `cat taking`. Both ways. It’s the highest form of admiration and appreciation. Besides, I needn’t a lecture. I’m quite aware, I’ve been around a long time. On and off from the beginning, or close to it. You know how many `cats` I haven’t been able to `steal` due to these rules? I’m sorry your infinitely replicable series of `cats` get used to make other things when you’re not lording over every `cat` in circulation. My deepest apologies. If you weren’t so good, at times, I’d be more blunt and heavy handed about this.")

    @commands.command()
    async def credit (self, ctx):
        """huwhwa"""
        await ctx.send("Yes, I do. I contacted the person who submitted/made it online. Right, of course, I'm not going to go stealing others' hard work, that's just wrong. What do you mean? I'm not trying to force people to help me, if that's what you're saying. That's why I said if anyone wants to help me, that'd be really appreciated. If I was forcing people to do it, I'd have said it with a threat, if that makes sense.")


    @commands.command()
    async def ears (self, ctx):
        """wtf"""
        await ctx.send(file=discord.File("./ears.png"))

    @commands.command()
    async def gotonap(self, ctx):
        "naptime"
        await ctx.send(file=discord.File("./gotonap.png"))

    @commands.command()
    async def hackradd(self, ctx):
        "is it tho?"
        await ctx.send(file=discord.File("./hackradd.png"))

    @commands.command()
    async def zanesjw(self, ctx):
        "the best sjw"
        await ctx.send(file=discord.File("./zanesjw.png"))

    @commands.command()
    async def yeszane(self, ctx):
        "skeleyes"
        await ctx.send(file=discord.File("./yeszane.jpg"))

    @commands.command()
    async def zane(self, ctx):
        "I agree with the skeleton"
        await ctx.send(file=discord.File("./zane.png"))

    @commands.command()
    async def topkek(self, ctx):
        "Off the top"
        await ctx.send(file=discord.File("./topkek.jpg"))

    @commands.command()
    async def nyeh(self, ctx):
        """skelepirate"""
        await ctx.send(file=discord.File("./nyeh.png"))

    @commands.command()
    async def hisworld(self, ctx):
        """sonic ememememee"""
        await ctx.send("https://www.youtube.com/watch?v=d2tdSiQAF20")

    @commands.command()
    async def work (self, ctx):
        """Gosh darn delinquents"""
        await ctx.send("Get back to work you maggots!!!")

    @commands.command()
    async def keriku (self, ctx):
        """Kelikringe"""
        await ctx.send("https://cdn.discordapp.com/attachments/261347653084905482/511231047254409217/Kookil_ket.webm")

    @commands.command()
    async def klek (self, ctx):
        """Kelik"""
        await ctx.send("`I invoke the wrath of`")
        await ctx.send("`Grant me the power to rid`")
        await ctx.send("`of these corrupt souls...`")

    @commands.command()
    async def thisdivinelightning (self, ctx):
        """The holy thunder"""
        await ctx.send("shall pierce the skies!")

    @commands.command()
    async def frenchzane (self, ctx):
        """Zane's truest form"""
        await ctx.send(file=discord.File("./paintmelikeoneofyourfrenchgirls.png"))

    @commands.command()
    async def wav2egg (self, ctx):
        """the big oof"""
        await ctx.send(file=discord.File("./wav2egg.png"))

    @commands.command()
    async def gotobed (self, ctx):
        """Listen to your doctors"""
        await ctx.send(file=discord.File("./gotobed.png"))

    @commands.command(aliases=["head"])
    async def useyourhead (self, ctx):
        """Way to use your head, Ephraim."""
        await ctx.send(file=discord.File("./head.gif"))

    @commands.command(aliases=["ketchup", "slurp"])
    async def drink (self, ctx):
        """But is it a smoothie??"""
        await ctx.send(file=discord.File("./Cheers.gif"))

    @commands.command()
    async def sain (self, ctx):
        """Horny horseman"""
        await ctx.send(file=discord.File("./Sain.jpeg"))

    @commands.command(aliases=["band"])
    async def theband (self, ctx):
        """I doubt the titanic was this dedicated"""
        await ctx.send(file=discord.File("./the band.gif"))

    @commands.command()
    async def whattime(self, ctx):
        """tells the time"""
        await ctx.send("`it's tiki time`")
        # await asyncio.sleep(1)
        await ctx.send(file=discord.File("tiki.gif"))

    @commands.command()
    async def orbit(self, ctx):
        """my tiki's"""
        await ctx.send(file=discord.File("Tikis_in_orbit.png"))

    @commands.command()
    async def writing(self, ctx):
        """get it in writing. in blood."""
        await ctx.send(file=discord.File("Pelleass_Blood_Pact.png"))

    @commands.command(name="wtf")
    async def wtfdyjfsamylb(self, ctx):
        """what the fuck did you just fucking say about me you little bitch"""
        await ctx.send("""```
What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the FE University, and I’ve been involved in numerous secret raids on Serenes Forest, and I have over 300 confirmed hacks. I am trained in donating to hex and I’m the top debugger in the entire FE Shrine. You are nothing to me but just another breakpoint. I will wipe you the fuck out with precision the likes of which has never been seen before on an ARMv7TDMI, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of backups across the ROM and your link register is being traced right now so you better prepare for the screech, fleshling. The death screech that wipes out the pathetic little thing you call your reskin. You’re fucking dead, kid. I can be anywhere, anytime, and I can crash your rom in over seven hundred ways, and that’s just with FEditor. Not only am I extensively trained in Nightmare, but I have access to the entire arsenal of the Unified FE Hacking Doc and I will use it to its full extent to wipe your miserable map sprite off the face of Magvel, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit Erin all over you and you will drown in it. You’re fucking dead, kiddo.
```""")

    @commands.command(name="ma???a")
    async def ma___a(self, ctx):
        """what IS her name anyway"""
        letters = [x for x in "abcdefghijklmnopqrstuvwyxz"]
        consonants = [x for x in "bcdfghjklmnpqrstvwxz"]
        vowels = [x for x in "aeiouy"]
        infix = random.choice(consonants) + random.choice(letters) + random.choice(vowels)
        await ctx.send("I think you mean Ma"+infix+"a!")

    @commands.command()
    async def evil(self, ctx, *args):
        """Sub-humans."""
        if len(args) > 0:
            thing = ' '.join(args)
            plural = thing[-1] == 's' #TODO: use inflect
            formatString = '''```\n{1} {0} evil.\n{1} {0} the enemy.\n{1} must be eradicated.```'''
            verb = "are" if plural else "is"
            await ctx.send(formatString.format(verb, thing))
        else:
            await ctx.send("You gotta tell me **what's** evil!")


    @commands.command()
    async def colorz(self, ctx):
        """do something with colorz"""
        direction = random.choice([":arrow_down:", ":arrow_up:"])
        await ctx.send(direction+" with <:colorz:230159530158194688>")


    @commands.command()
    async def style(self, ctx):
        """if my style gets in your way"""
        img = random.choice(["styleRD.gif", "stylePoR.jpeg"])
        await ctx.send(file=discord.File(img))


    @commands.command()
    async def whois(self, ctx,*args):
        """roy is our boy"""
        if len(args) > 0:
            lord = ' '.join(args)
            if (lord.lower() in ['circles','circleseverywhere']):
                await ctx.send(lord + " is my dad")
                return
            elif (lord.lower() == 'feditor'):
                await ctx.send("`" + lord + " a shit`")
                return
            elif (lord.lower() == 'feubot'):
                await ctx.send("That's me, silly!")
                return
            elif (lord.lower() == 'ea'):
                await ctx.send("`" + lord + " is our bae`")
                return
            elif (lord.lower() in ['bm', 'blackmage', 'black mage']):
                await ctx.send(file=discord.File("BMis.gif"))
                return
            elif lord[0].lower() in 'bcdfghjklmnpqrstvwxz':
                blord = 'b'+lord[1:]
            else:
                blord = 'b'+lord
            await ctx.send(lord + " is our " + blord)

    @commands.command()
    async def createwaifu(self, ctx,*args):
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
            "<:dootthunk:339479700147798016>",
            "<:doot:324593825815461889>",
            "<:donate:230166446146191362>",
            "<:doc:280527122802540544>",
            "<:colorz:230159530158194688>",
            "<:circles:238177111418863617>",
            "<:celica:272027128231362571>",
            "<:BBQ:230169373694885888>",
            "<:arch_mini:230160993299202068>",
            "<:camthumb:307559627573428224>",
            "<:dat:292422389197701121>",
            "<:thighs:294965155819683840>"]
        if len(args) > 0: head = ' '.join(args)
        else: head = random.choice(heads)
        await ctx.send(head + """
<:personality:385616854451748864>
<:thighs:294965155819683840>""")


    @commands.command(aliases=["(lol"])
    async def lol(self, ctx):
        """(lol"""
        flip = random.choice([0,1])
        if flip==1: await ctx.send(file=discord.File("./Water_lol.png"))
        else: await ctx.send(file=discord.File("./Water_lol2.png"))

    @commands.command(aliases=["eventassembler", "everythingassembler"])
    async def ea(self, ctx):
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
        await ctx.send(everythingassemblerstring)

    @commands.command()
    async def casual(self, ctx):
        """just play phoenix"""
        barflist = os.listdir("./casual")
        await ctx.send(file=discord.File("./casual/"+random.choice(barflist)))


    @commands.command()
    async def slow(self, ctx):
        """It's what I ain't."""
        await ctx.send(file=discord.File("./slow.png"))


    @commands.command(aliases=["SOA", 'SoA'])
    async def soa(self, ctx):
        """there's your problem"""
        await ctx.send(file=discord.File("./SoA.png"))

    @commands.command()
    async def hard(self, ctx):
        """HARD"""
        await ctx.send(file=discord.File("./hard.png"))

    @commands.command()
    async def goof(self, ctx, *args):
         """show goof"""
         requested = args
         gooflist = os.listdir("./goofs")
         if len(requested) != 0:
             for request in requested:
                if request in gooflist:
                    await ctx.send(file=discord.File("./goofs/"+request+".png"))
                else:
                    await ctx.send("Use >>goofs to see a list of accepted goofs.")
         else:
             await ctx.send(file=discord.File("./goofs/"+random.choice(gooflist)))

        

    @commands.command()
    async def donate(self, ctx):
        """you know it"""
        await ctx.send("https://www.patreon.com/theFEUfund")
        await ctx.send("https://donorbox.org/donate-to-circles")


    @commands.command()
    async def UT2(self, ctx):
        """links ultimate tutorial v2"""
        await ctx.send("https://stackedit.io/viewer#!provider=gist&gistId=084645b0690253600f4aa2a57b76a105&filename=feutv2")

    @commands.command()
    async def reply(self, ctx):
        """r e p l y s o o n"""
        await ctx.send("reply :soon: :smile:")

    @commands.command()
    async def arch(self, ctx):
        """do something with arch"""
        direction = random.choice([":arrow_down:", ":arrow_up:", ":arrow_up_down:", ":question:", ":heart:"])
        await ctx.send(direction+" with <:arch_mini:230160993299202068>")

    @commands.command()
    async def goofs(self, ctx):
        """list goofs"""
        await ctx.send("```"+"\n".join(map(str, os.listdir("./goofs")))+"```")
    
    @commands.command()
    async def erin(self, ctx):
        """ERIN INTENSIFIES"""
        await ctx.send(file=discord.File("./erinyous.gif"))

    @commands.command()
    async def fury(self, ctx):
        """2 FAST 2 FURYOUS"""
        await ctx.send("Don't you mean `>>erin`?")

    @commands.command()
    async def doot(self, ctx):
        """doot doot"""
        await ctx.send("""<:doot:324593825815461889> <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> <:doot:324593825815461889> <:doot:324593825815461889>
    <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
    <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
    <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
    <:doot:324593825815461889> <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:""")


    
def setup(bot):
    bot.add_cog(Memes(bot))
