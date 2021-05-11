import aiohttp
import discord
import asyncio
import time
from discord.ext import commands

class general(commands.Cog, name="General"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """ Get the bot latency """
        da = time.monotonic()
        async with aiohttp.ClientSession() as a:
            async with a.get("https://discord.com") as r:
                if r.status == 200:
                    de = time.monotonic()
                    dms = f"{round((de - da) * 1000)}ms"
                else:
                    dms = "Discord has died!"
                await ctx.reply("My ping is **" + dms + "**.")


def setup(bot):
    bot.add_cog(general(bot))