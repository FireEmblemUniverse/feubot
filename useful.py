import discord
from discord.ext import commands as bot
import urllib
import urllib.request
import urllib.error
import json
import asyncio
import re
import random
import os
import aiohttp

def trunc_to(ln, s):
    if len(s) <= ln: return s
    else: return s[:ln-3] + "..."

def highlight(s, term, type='**'):
    to_bold = term.split(' ')
    output = re.sub(r'(%s)' % '|'.join(to_bold), (type + r'\1' + type), s, flags=re.IGNORECASE)
    return output

def capitalise(s, term):
    to_bold = term.split(' ')
    output = re.sub(r'(%s)' % '|'.join(to_bold), lambda match: r'{}'.format(match.group(1).upper()), s, flags=re.IGNORECASE)
    return output

def linkify(searchtext):
    feu_post_base = "http://feuniverse.us/t/{}/{}"
    def result(data):
        post, thread = data
        title = highlight(thread['title'], searchtext, '*')
        blurb = highlight(trunc_to(100, post['blurb']), searchtext)
        link = '[Post in %s](%s)' % (
                title,
                feu_post_base.format(post['topic_id'], post['post_number']))
        threadline = '**%s by %s**' % (link, highlight(post['username'], searchtext, '*'))
        return threadline + '\n' + blurb
    return result

def create_embed(posts, threads, term):
    feu_search_base = "http://feuniverse.us/search?q=%s"
    searchtext = urllib.parse.unquote(term)

    numresults = 3

    result = discord.Embed(
            title='Search results for "%s"' % urllib.parse.unquote(term),
            url=feu_search_base % term,
            color=0xde272c)
    if len(posts)>0:
        innerEmbed = '\n\n'.join(
                map(linkify(searchtext),zip(posts[:numresults],threads)))
        result.add_field(
                name='Found %d result(s)' % len(posts),
                value=innerEmbed,
                inline=False)
    else:
        result.description = 'Found %d result(s)' % len(posts)
    if len(posts) > numresults:
        result.set_footer(
                text="Truncated %d result(s)." % (len(posts)-numresults))
    return result

class Useful:
    """Actually useful commands"""

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def ut2(self):
        """links ultimate tutorial v2"""
        embed=discord.Embed(title="Fire Emblem Hacking Ultimate Tutorial v2", url='https://stackedit.io/viewer#!provider=gist&gistId=084645b0690253600f4aa2a57b76a105&filename=feutv2', description="How to do everything with Event Assembler buildfiles", color=0x40caf2)
        await self.bot.say(embed=embed)

    @bot.command()
    async def search(self, *, term):
        """search feu"""
        root = "http://feuniverse.us/search.json?q=%s"
        payload = urllib.parse.quote(term)

        async with aiohttp.ClientSession() as session:
            async with session.get(root % payload) as response:
                data = await response.json()
        # async with aiohttp.get(root % payload) as query:
        # # with urllib.request.urlopen(root % payload) as query:
        #     if query.status == 200:
        #         data = await query.json()
            try:
                # data = json.loads(js.read().decode())
                posts = data["posts"]
                threads = data["topics"]
                await self.bot.say(embed=create_embed(posts, threads, payload))
            except urllib.error.URLError:
                await self.bot.say("Error accessing FEU server, please try again later.")
            except KeyError:
                embedded=create_embed(posts, [], payload)
                try:
                    await self.bot.say(embed=embedded)
                except discord.errors.HTTPException:
                    print(embedded.title)

    @bot.command()
    async def hit(self, number, type="1RN"):
        """rolls hit or miss (e.g. >>hit 50 1rn[default]/2rn/fates)"""
        try:
            num = int(number)
        except ValueError:
            await self.bot.say("Specify an integer 0-100")
            return
        if (num < 0) or (num > 100):
            await self.bot.say("Specify an integer 0-100")
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
            await self.bot.say("Valid types are 1RN, 2RN, Fates")
            return
        if rolled <= num: await bot.say("HIT (%d)" % rolled)
        else: await self.bot.say("MISS (%d)" % rolled)

    @bot.command()
    async def goldmine(self):
        """everything you ever wanted"""
        embed=discord.Embed(title="Unified FE Hacking Dropbox", url='https://www.dropbox.com/sh/xl73trcck2la799/AAAMdpNSGQWEzYkLEQEiEhGFa?dl=0', description="All the hacking resources you could ever need, in one place", color=0xefba01)
        # embed.set_thumbnail(url='http://i.imgur.com/Bg5NSga.png')
        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(Useful(bot))
