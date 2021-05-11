import discord
import traceback
from vars import pycogs, tokens

from discord.ext import commands


bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('e?'),
    case_insensitive=True,
    max_messages=10000,
    intents=discord.Intents.all(),
    status=discord.Status.dnd,
    activity=discord.Activity(type=discord.ActivityType.playing, name='with APIs'),
    description="A discord bot that connects with many APIs to provide a ton of information, images and other things."
)

@commands.Cog.listener()
async def on_ready():
    print(f'[READY] {bot.user} has started successfully.')

for extension in pycogs.extensions:
    try:
        bot.load_extension(extension)
        print(f'[EXTENSION] {extension} was loaded successfully!')
    except Exception as e:
        tb = traceback.format_exception(type(e), e, e.__traceback__)
        tbe = "".join(tb) + ""
        print(f'[WARNING] Could not load extension {extension}: {tbe}')

bot.run(tokens.bot)