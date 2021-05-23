import discord
import config
import traceback

from discord.ext import commands


bot = commands.AutoShardedBot(
    command_prefix=commands.when_mentioned_or('e.'),
    intents=discord.Intents.all(),
    max_messages=5000,
    status=discord.Status.online,
    activity=discord.Activity(type=discord.ActivityType.playing, name=f'With my maker'),
    description=f"Providing my users with plenty of commands to provide information, images and more through APIs."
)

for extension in config.extensions:
    try:
        bot.load_extension(extension)
        print(f'[EXTENSION] {extension} has loaded successfully.')
    except Exception as e:
        tb = traceback.format_exception(type(e), e, e.__traceback__)
        tbe = "".join(tb) + ""
        print(f'[WARNING] Could not load extension {extension}: {tbe}')

bot.run(config.bottoken)
