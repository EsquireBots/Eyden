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

    @commands.command(aliases=['aq', 'animequote'])
    @commands.cooldown(1, 5, commands.BucketType.user)
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
    async def xkcd(self, ctx, comic: int=None): # Add comic=none
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

        #text = _("**Search:** {0}\n**Author:** {1}\n"
        #         "{2} {3} | {4} {5}\n**Definition:**\n{6}\n"
        #         "**Example:**\n{7}").format(result['word'], result['author'], self.bot.settings['emojis']['misc']['upvote'],
        #                                     result['thumbs_up'], self.bot.settings['emojis']['misc']['downvote'], result['thumbs_down'],
        #                                     definition, example)
        await ctx.send(embed=e)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
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
            return await ctx.send(f"Please provide an **existent** pokemon.\n" \
                                   "*If the pokemon you sent does exist, the API might be down.*")


def setup(bot):
    bot.add_cog(media(bot))
