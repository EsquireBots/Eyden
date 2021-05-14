import discord
import traceback

from discord.ext import commands


class error(commands.Cog, name="Errors"):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if isinstance(err, commands.CommandNotFound):
            return

        if isinstance(err, commands.NSFWChannelRequired):
            return await ctx.send(":no_entry: This command is only available in **nsfw channels**.")


def setup(bot):
    bot.add_cog(error(bot))
