import aiohttp
import discord
import random

from discord.ext import commands


class animals(commands.Cog, name="animals"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fox(self, ctx):
        """ Spot some foxes! """
        rdmf = random.choice(["https://randomfox.ca/floof/", "https://some-random-api.ml/img/fox"])

        async with aiohttp.ClientSession() as session:
            async with session.get(rdmf) as r:
                js = await r.json()

                e = discord.Embed(color=discord.Color.orange())
                e.set_image(url=js['image'] if rdmf == "https://randomfox.ca/floof/" else js['link'])

                await ctx.send(f"Enjoy the random {ctx.command.qualified_name} ^w^", embed=e)

    @commands.command()
    async def cat(self, ctx):
        """ Spot some cats! """
        rdmc = random.choice(["https://thatcopy.pw/catapi/rest/", "https://api.thecatapi.com/v1/images/search", "https://aws.random.cat/meow"])

        async with aiohttp.ClientSession() as session:
            async with session.get(rdmc) as r:
                js = await r.json()

                e = discord.Embed(color=discord.Color.random())
                e.set_image(url=js['url'] if rdmc == "https://thatcopy.pw/catapi/rest/" else js['file'] if rdmc == "https://aws.random.cat/meow" else js[0]['url'])
                e.set_footer(text=js['url'] if rdmc == "https://thatcopy.pw/catapi/rest/" else js['file'] if rdmc == "https://aws.random.cat/meow" else js[0]['url'])

                await ctx.send(f"Enjoy the random {ctx.command.qualified_name} ^w^", embed=e)

    @commands.command()
    async def dog(self, ctx):
        """ Spot some dogs! """
        rdmd = random.choice(["https://shibe.online/api/shibes", "https://dog.ceo/api/breeds/image/random", "https://random.dog/woof.json"])

        async with aiohttp.ClientSession() as session:
            async with session.get(rdmd) as r:
                js = await r.json()

                e = discord.Embed(color=discord.Color.random())
                e.set_image(url=js[0] if rdmd == "https://shibe.online/api/shibes" else js['message'] if rdmd == "https://dog.ceo/api/breeds/image/random" else js['url'])
                e.set_footer(text=js[0] if rdmd == "https://shibe.online/api/shibes" else js['message'] if rdmd == "https://dog.ceo/api/breeds/image/random" else js['url'])
                await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(animals(bot))
