import discord
from discord.ext import commands
from datetime import datetime
from utils import default
from settings import channels


class guilds(commands.Cog, name="Guilds"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        print(f"{datetime.now().__format__('%a %d %b %y, %H:%M')} - {ctx.guild.name} | {ctx.author} > {ctx.message.clean_content}")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        log = self.bot.get_channel(channels.guildlogs)
        owner = await self.bot.fetch_user(guild.owner_id)
        owner = str(owner)

        gl = discord.Embed(color=discord.Color.green(), title="New guild joined")
        gl.set_author(name=guild, icon_url=guild.icon_url)
        gl.set_footer(text=f"Now in {len(self.bot.guilds)} guilds")
        gl.description = f"""
Guild **{guild}** ({guild.id})
Owner: **{owner}** ({guild.owner_id})
Created on **{default.date(guild.created_at)}**
Approximately **{guild.member_count}** members
**{len(guild.text_channels)}** text & **{len(guild.voice_channels)}** voice channels
Icon url: **[Click here]({guild.icon_url})** 
"""

        await log.send(guild.id, embed=gl)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        log = self.bot.get_channel(channels.guildlogs)
        owner = await self.bot.fetch_user(guild.owner_id)
        owner = str(owner)

        gl = discord.Embed(color=discord.Color.red(), title="Old guild left")
        gl.set_author(name=guild, icon_url=guild.icon_url)
        gl.set_footer(text=f"Now in {len(self.bot.guilds)} guilds")
        gl.description = f"""
        Guild **{guild}** ({guild.id})
        Owner: **{owner}** ({guild.owner_id})
        Created on **{default.date(guild.created_at)}**
        Approximately **{guild.member_count}** members
        **{len(guild.text_channels)}** text & **{len(guild.voice_channels)}** voice channels
        Icon url: **[Click here]({guild.icon_url})** 
        """

        await log.send(embed=gl)


def setup(bot):
    bot.add_cog(guilds(bot))
