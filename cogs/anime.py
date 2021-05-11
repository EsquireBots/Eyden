import discord
import aiohttp

from discord.ext import commands


class anime(commands.Cog, name="Anime"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["aq", "animequote"])
    async def aniquote(self, ctx):
        """ Get an anime quote! """
        async with aiohttp.ClientSession() as session:
            async with session.get("https://animechan.vercel.app/api/random") as r:
                js = await r.json()

                e = discord.Embed(color=discord.Color.pink())
                e.set_author(name=f"{js['character']} | from {js['anime']}")
                e.description = js['quote']

                await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(anime(bot))
