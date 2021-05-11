import aiohttp
import discord
import asyncio
import time

from collections import Counter
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

    @commands.command()
    async def about(self, ctx):
        """ About Eyden """

        def date(target, clock=True):
            if clock is False:
                return target.strftime("%d %B %Y")
            return target.strftime("%d %B %Y, %H:%M")

        Flitz = await self.bot.fetch_user(809057677716094997)

        chtypes = Counter(type(c) for c in self.bot.get_all_channels())
        voice = chtypes[discord.channel.VoiceChannel]
        text = chtypes[discord.channel.TextChannel]

        e = discord.Embed(color=discord.Color.baby_blue())
        e.set_author(name=f"About {self.bot.user}", icon_url=self.bot.user.avatar_url)
        e.set_thumbnail(url=self.bot.user.avatar_url)
        e.description = f"""
Created by **{str(Flitz)}**
Created on **{date(self.bot.user.created_at)}**

Library **discord.py** on version **{discord.__version__}**
Links: **[fill in desired hyperlinks here]**

Commands: **{len([c for c in set(self.bot.walk_commands())])}**
Guilds: **{len(self.bot.guilds)}**
Users: **{sum(x.member_count for x in self.bot.guilds)}**
**{text:,} text** channels & **{voice:,} voice** channels

{self.bot.description}
"""
        await ctx.reply(embed=e)

def setup(bot):
    bot.add_cog(general(bot))