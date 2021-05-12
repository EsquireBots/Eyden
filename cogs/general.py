import discord
import aiohttp
import time

from settings import links, emotes
from utils.default import date
from collections import Counter
from discord.ext import commands


class general(commands.Cog, name="Generic"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ping(self, ctx):
        """ See bot's latency to discord """
        discord_start = time.monotonic()
        async with aiohttp.ClientSession() as session:
            async with session.get('https://discord.com') as r:
                if r.status == 200:
                    discord_end = time.monotonic()
                    discord_ms = f"{round((discord_end - discord_start) * 1000)}ms"
                else:
                    discord_ms = "fucking dead"
                await ctx.send(f"My ping is **{discord_ms}**")  # You can use :ping_pong: instead of \U0001f3d3

    @commands.command()
    async def about(self, ctx):
        """ About Eyden """

        Flitz = await self.bot.fetch_user(809057677716094997)

        chtypes = Counter(type(c) for c in self.bot.get_all_channels())
        voice = chtypes[discord.channel.VoiceChannel]
        text = chtypes[discord.channel.TextChannel]

        e = discord.Embed(color=discord.Color.blurple())
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
"""
        await ctx.reply(embed=e)

    @commands.command()
    async def support(self, ctx):
        """ Get support with Eyden! """
        Flitz = await self.bot.fetch_user(809057677716094997)

        e = discord.Embed(color=discord.Color.blue())
        e.set_author(name=f"Get help with {self.bot.user} here!", icon_url=self.bot.user.avatar_url)
        e.description = f"[Support server]({links.support})\n" \
                        f"[Message {str(Flitz)}]({links.Flitzdiscord})"
        await ctx.send(embed=e)

    @commands.command()
    async def invite(self, ctx):
        """ Get an invite! """
        e = discord.Embed(color=discord.Color.blue())
        e.set_author(name=f"Invite {self.bot.user} here!", icon_url=self.bot.user.avatar_url)
        e.description = f"{emotes.discovery} [Admin invite link]({links.Invite_admin})"
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(general(bot))
