
from time import time

import discord
from discord.ext import commands as bot

_TIMEOUT = 60
_PERMITTED_ROLES = ['Paladins', 'Lords', 'Mage Knights']

_cache = None

class DeletedCache(dict):
    def __getitem__(self, key):
        reqt = time()
        try:
            result, ts = dict.__getitem__(self, key)
        except KeyError:
            return None
        else:
            if reqt-ts >= _TIMEOUT:
                self.__delitem__(key)
                return None
            return result

    def __setitem__(self, key, value):
        addt = time()
        self.mostrecent = (value, addt)
        dict.__setitem__(self, key, (value, addt))

    def last(self):
        reqt = time()
        if self.mostrecent is not None:
            result, ts = self.mostrecent
            if reqt-ts >= _TIMEOUT:
                self.mostrecent = None
                return None
            return result
        return None

    def __init__(self):
        self.mostrecent = None
        super().__init__()

class UndeleteCog(object):
    FORMAT = '{0.author} said:\n```{0.content}```'
    __slots__ = ['bot']

    @bot.command(pass_context=True, hidden=True)
    async def undelete(self, ctx, *, name=None):
        msg = ctx.message
        if (type(msg.author) is discord.Member
            and not [r for r in msg.author.roles
                           if str(r) in _PERMITTED_ROLES]
        ):
            await self.bot.say('You do not have undelete permissions.')
            return
        if name is None:
            if _cache.last() is not None:
                await self.bot.say(
                        UndeleteCog.FORMAT.format(_cache.last()))
            else:
                await self.bot.say(
                        'No messages deleted within the last minute')
            return
        if _cache[name] is not None:
            await self.bot.say(UndeleteCog.FORMAT.format(_cache[name]))
        else:
            await self.bot.say(
                    'No messages deleted by %s within the last minute'
                    % name)

    def __init__(self, bot):
        global _cache
        _cache = DeletedCache()
        self.bot = bot

def cache(msg):
    if type(msg.author) is discord.User:
        print('Caching deletion from %s' % msg.author.name)
    _cache[msg.author.name] = msg

def setup(bot):
    bot.add_cog(UndeleteCog(bot))

