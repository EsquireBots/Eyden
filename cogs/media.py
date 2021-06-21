import json
import random
import aiohttp
import discord

from discord.ext import commands
from settings import emotes

import config


class media(commands.Cog, name="Media"):
    def __init__(self, bot):
        self.bot = bot
        self.help_icon = '🔗'

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
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
    @commands.bot_has_permissions(embed_links=True)
    async def dog(self, ctx):
        """ Get a random dog """
        rdmd = random.choice(['http://shibe.online/api/shibes?count=1', 'https://dog.ceo/api/breeds/image/random',
                              'https://random.dog/woof.json', 'https://some-random-api.ml/img/dog'])
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
    @commands.bot_has_permissions(embed_links=True)
    async def cat(self, ctx):
        """ Get a random cat """
        rdmc = random.choice(
            ['https://thatcopy.pw/catapi/rest/', 'https://aws.random.cat/meow', 'http://shibe.online/api/cats?count=1',
             'https://some-random-api.ml/img/cat'])
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

    @commands.command(aliases=['aq', 'animequote'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def aniquote(self, ctx):
        """ Get a random anime quote """
        session = aiohttp.ClientSession()
        r = await session.get('https://animechan.vercel.app/api/random')
        js = await r.json()

        e = discord.Embed(color=discord.Color.purple())
        e.set_author(name=js['character'] + " from " + js['anime'])
        e.description = js['quote']

        await session.close()
        await ctx.send(embed=e)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def xkcd(self, ctx, comic: int = None):
        """ Get an xkcd comic """
        if comic is None:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://xkcd.com/{random.randint(1, 2462)}/info.0.json") as r:
                    js = await r.json()

                    e = discord.Embed(color=discord.Color.dark_gray())
                    e.set_image(url=js['img'])

                    await ctx.send(embed=e)
        else:
            if comic > 2462:
                return await ctx.send('There are only 2462 comics.')

            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://xkcd.com/{comic}/info.0.json") as r:
                    js = await r.json()

                    e = discord.Embed(color=discord.Color.dark_gray())
                    e.set_image(url=js['img'])

                    await ctx.send(embed=e)

    @commands.command()
    @commands.dm_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def mailcheck(self, ctx, mail):
        """ Get data about an email """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://apilayer.net/api/check?access_key={config.mbltoken}&email={mail}") as r:
                js = await r.json()

        try:
            e = discord.Embed(color=discord.Color.green())
            e.set_footer(text="Powered by apilayer.net")
            e.add_field(name=js['email'],
                        value=f"""
**Domain:** {js['domain']}
**Format:** {js['format_valid']}
**Mail exchange (record):** {js['mx_found']}
**SMTP check:** {js['smtp_check']}
**Catch-all:** {js['catch_all']}
**Role based:** {js['role']}
**Disposable:** {js['disposable']}
**Free:** {js['free']}

**Overall score:** {js['score']}
""")

            await ctx.send(embed=e)
        except Exception:
            try:
                e = discord.Embed(color=discord.Color.red())
                e.description = f"Error {js['error']['code']}: {js['error']['type'].replace('_', ' ').capitalize()}\n" \
                                f"**{js['error']['info']}**"
                await ctx.send(embed=e)
            except Exception as e:
                await ctx.send(f'Error getting data:\n{e}')

    @commands.command(brief="Search the urban dictionary")
    @commands.guild_only()
    @commands.is_nsfw()
    async def urban(self, ctx, *, urban: str):
        """ Search for a term in the urban dictionary """

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'http://api.urbandictionary.com/v0/define?term={urban}') as r:
                url = await r.json()

        if url is None:
            return await ctx.send("No URL found")

        count = len(url['list'])
        if count == 0:
            return await ctx.send("No results were found.")
        result = url['list'][random.randint(0, count - 1)]

        definition = result['definition']
        example = result['example']
        if len(definition) >= 1000:
            definition = definition[:1000]
            definition = definition.rsplit(' ', 1)[0]
            definition += '...'

        e = discord.Embed(color=discord.Color.blue())
        e.set_author(name=result['author'])
        e.description = definition
        e.add_field(name="Example",
                    value=example)
        e.set_footer(text=f"{ctx.author} searched {result['word']}")
        await ctx.send(embed=e)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def pokemon(self, ctx, pokemon):
        """ Get pokemon info """
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}") as r:
                    js = await r.json()

                async with cs.get(f"https://some-random-api.ml/pokedex?pokemon={pokemon}") as t:
                    js1 = await t.json()

                abilities = []
                for x in js['abilities']:
                    abilities.append(f"[{x['ability']['name'].replace('-', ' ').capitalize()}]({x['ability']['url']})")

                type = []
                for x in js['types']:
                    type.append(f"[{x['type']['name'].replace('-', ' ').capitalize()}]({x['type']['url']})")

                e = discord.Embed(color=discord.Color.dark_teal())
                # e.set_author(name=js['caption'])
                e.title = js['name'].capitalize() + f" Evo. stage {js1['family']['evolutionStage']}"
                e.description = f"""
*Read everything on [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/{pokemon}_(Pok%C3%A9mon))*
**Abilities:** {", ".join(abilities)}
**Type:** {", ".join(type)}
**Description:** {js1['description']}
**Evolution:** {' - '.join(js1['family']['evolutionLine'])}
**Egg groups:** {', '.join(js1['egg_groups'])}
**Species:** {', '.join(js1['species'])}
"""
                st = js1['stats']
                e.set_thumbnail(url=js['sprites']['other']['official-artwork']['front_default'])
                e.add_field(name="Statistics",
                            value=f"**{st['hp']}** HP\n" \
                                  f"**{st['attack']}** Attack\n" \
                                  f"**{st['defense']}** Defense\n" \
                                  f"**{st['sp_atk']}** Special Attack\n" \
                                  f"**{st['sp_def']}** Special Defense\n" \
                                  f"**{st['speed']}** Speed")
                e.set_footer(text="Made using some-random-api & pokeapi")
                await ctx.send(embed=e)
        except Exception:
            return await ctx.send(f"Please provide an **existent** pokemon.\n*If the pokemon you sent does exist, the API might be down.*")

    @commands.command(aliases=['activity'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def bored(self, ctx):
        """ Get a random activity """
        session = aiohttp.ClientSession()
        r = await session.get("https://boredapi.com/api/activity")
        js = await r.json()

        e = discord.Embed(color=discord.Color.green())
        e.add_field(name='type' + js['type'],
                    value=js['activity'])
        e.set_footer(text="Powered by boredapi.com")
        await session.close()
        await ctx.send(embed=e)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def food(self, ctx, food: str = None):
        """ Get food images! """
        try:
            if food == None:

                session = aiohttp.ClientSession()
                r = await session.get("https://foodish-api.herokuapp.com/api")
                js = await r.json()

                e = discord.Embed(color=discord.Color.random())
                e.set_image(url=js['image'])
                e.set_footer(text="Powered by foodish-api")

                await session.close()
                await ctx.send(embed=e)

            else:
                session = aiohttp.ClientSession()
                r = await session.get(f"https://foodish-api.herokuapp.com/api/images/{food}")
                js = await r.json()

                e = discord.Embed(color=discord.Color.random())
                e.set_image(url=js['image'])
                e.set_footer(text="Powered by foodish-api")

                await session.close()
                await ctx.send(embed=e)
        except Exception:
            try:
                await ctx.send(emotes.cross + " " + js['error'])
                await session.close()
            except Exception as e:
                await ctx.send(f'Error getting data:\n{e}')
                await session.close()

    @commands.command(aliases=["insult"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def evilinsult(self, ctx):
        """ Get a random insult """
        session = aiohttp.ClientSession()
        r = await session.get("https://evilinsult.com/generate_insult.php?type=json")
        js = await r.json()

        await session.close()
        await ctx.send(js['insult'])

    @commands.command(aliases=['advise'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def advice(self, ctx):
        """ Get random advice """
        session = aiohttp.ClientSession()
        resp = await session.get(f"https://api.adviceslip.com/advice")
        text = await resp.text()
        js = json.loads(text)

        await session.close()
        await ctx.send(js['slip']['advice'])

    @commands.command(aliases=['urlshorten', 'shorten'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def urlshortener(self, ctx, url):
        """ Shorten a url """
        session = aiohttp.ClientSession()
        resp = await session.get(f"https://is.gd/create.php?format=json&url={url}")
        text = await resp.text()
        js = json.loads(text)

        await session.close()
        await ctx.send(js['shorturl'])
 
    @commands.command(aliases=['Apod', 'Astronomy pic'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def apod(self, ctx):
        session = aiohttp.ClientSession()
        r = await session.get(f"https://api.nasa.gov/planetary/apod?api_key={config.napi}")
        js = await r.json()
        if 'copyright' not in js:
            js['copyright'] = f"NASA"
         
        e = discord.Embed(color=discord.Color.random(), title=f"{js['date']}", description=f"{js['explanation']}")
        e.set_image(url=js['hdurl'])
        e.set_footer(text=js['copyright'])
        
       
        await session.close()
        await ctx.send(embed=e)
    


def setup(bot):
    bot.add_cog(media(bot))
