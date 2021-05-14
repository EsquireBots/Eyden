import random
import aiohttp
import discord

from discord.ext import commands


class media(commands.Cog, name="Media"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fox(self, ctx):
        """ Get a random fox """
        rdmf = random.choice(['https://randomfox.ca/floof/', 'https://some-random-api.ml/img/fox'])
        session = aiohttp.ClientSession()
        r = await session.get(rdmf)
        js = await r.json()

        e = discord.Embed(color=discord.Color.orange())
        e.set_image(url=js['image'] if rdmf == 'https://randomfox.ca/floof/' else js['link'])
        e.set_footer(text='Powered by randomfox.ca' if rdmf == 'https://randomfox.ca/floof/' else 'Powered by some-random-api.ml')

        await session.close()
        await ctx.send(embed=e)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, ctx):
        rdmf = random.choice(['http://shibe.online/api/shibes?count=1', 'https://dog.ceo/api/breeds/image/random', 'https://random.dog/woof.json', 'https://some-random-api.ml/img/dog'])
        session = aiohttp.ClientSession()
        r = await session.get(rdmf)
        js = await r.json()

        e = discord.Embed(color=discord.Color.random())
        e.set_image(url=js[0] if rdmf == 'http://shibe.online/api/shibes?count=1' else js['message'] if rdmf == 'https://dog.ceo/api/breeds/image/random' else js['url'] if rdmf == 'https://random.dog/woof.json' else js['link'])
        e.set_footer(text='Powered by shibe.online' if rdmf == 'http://shibe.online/api/shibes?count=1' else 'Powered by dog.ceo' if rdmf == 'https://dog.ceo/api/breeds/image/random' else 'Powered by random.dog' if rdmf == 'https://random.dog/woof.json' else 'Powered by some-random-api.ml')

        await session.close()
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(media(bot))
