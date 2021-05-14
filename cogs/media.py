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
        if rdmf == 'https://randomfox.ca/floof/':
            e.set_image(url=js['image'])
            e.set_footer(text="Powered by randomfox.ca")

        elif rdmf == 'https://some-random-api.ml/img/fox':
            e.set_image(url=js['link'])
            e.set_footer(text="Powered by some-random-api.ml")

        else:
            await session.close()
            await ctx.send('Something went wrong, please try again later.')

        await session.close()
        await ctx.send(embed=e)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, ctx):
        """ Get a random dog """
        rdmd = random.choice(['http://shibe.online/api/shibes?count=1', 'https://dog.ceo/api/breeds/image/random', 'https://random.dog/woof.json', 'https://some-random-api.ml/img/dog'])
        session = aiohttp.ClientSession()
        r = await session.get(rdmd)
        js = await r.json()

        e = discord.Embed(color=discord.Color.random())
        if rdmd == 'http://shibe.online/api/shibes?count=1':
            e.set_image(url=js[0])
            e.set_footer(text="Powered by shibe.online")

        elif rdmd == 'https://dog.ceo/api/breeds/image/random':
            e.set_image(url=js['message'])
            e.set_footer(text="Powered by dog.ceo")

        elif rdmd == 'https://random.dog/woof.json':
            e.set_image(url=js['url'])
            e.set_footer(text="Powered by random.dog")

        elif rdmd == 'https://some-random-api.ml/img/dog':
            e.set_image(url=js['link'])
            e.set_footer(text="Powered by some-random-api.ml")

        else:
            await session.close()
            await ctx.send('Something went wrong, please try again later.')

        await session.close()
        await ctx.send(embed=e)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cat(self, ctx):
        """ Get a random cat """
        rdmc = random.choice(['https://thatcopy.pw/catapi/rest/', 'https://aws.random.cat/meow', 'http://shibe.online/api/cats?count=1', 'https://some-random-api.ml/img/cat'])
        session = aiohttp.ClientSession()
        r = await session.get(rdmc)
        js = await r.json()

        e = discord.Embed(color=discord.Color.random())
        if rdmc == 'https://thatcopy.pw/catapi/rest/':
            e.set_image(url=js['url'])
            e.set_footer(text="Powered by thatcopy.pw")

        elif rdmc == 'https://aws.random.cat/meow':
            e.set_image(url=js['file'])
            e.set_footer(text="Powered by aws.random.cat")

        elif rdmc == 'http://shibe.online/api/cats?count=1':
            e.set_image(url=js[0])
            e.set_footer(text="Powered by shibe.online")

        elif rdmc == 'https://some-random-api.ml/img/cat':
            e.set_image(url=js['link'])
            e.set_footer(text="Powered by some-random-api.ml")

        else:
            await session.close()
            await ctx.send('Something went wrong, please try again later.')

        await session.close()
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(media(bot))
