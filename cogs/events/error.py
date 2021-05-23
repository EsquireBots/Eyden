from discord.ext import commands
from settings import emotes


class error(commands.Cog, name="Errors"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if isinstance(err, commands.CommandNotFound):
            return

        if isinstance(err, commands.NSFWChannelRequired):
            return await ctx.send(f"{emotes.cross} **This command is only available in nsfw channels**.")

        if isinstance(err, commands.CommandOnCooldown):
            return await ctx.send(f"{emotes.cooldown} **`{ctx.command.qualified_name.capitalize()}` is under cooldown for {err.retry_after:.0f} more seconds.**")

        if isinstance(err, commands.PrivateMessageOnly):
            return await ctx.send(f"{emotes.cross} **This command can only be used in Direct Messages.**")

        if isinstance(err, commands.NoPrivateMessage):
            return await ctx.send(f"{emotes.cross} **This command can only be used in guilds.**")

        if isinstance(err, commands.MissingRequiredArgument):
            return await ctx.send(f"{emotes.discovery} **You are missing required arguments - {err.param}**")

        if isinstance(err, commands.MissingPermissions):
            perms = "`" + '`, `'.join(err.missing_perms) + "`"
            return await ctx.send(f"{emotes.cross} **You are missing permissions - {perms.replace('_', ' ')}**")

        if isinstance(err, commands.BotMissingPermissions):
            perms = "`" + '`, `'.join(err.missing_perms) + "`"
            return await ctx.send(f"{emotes.cross} **I am missing permissions - {perms.replace('_', ' ')}**")

        if isinstance(err, commands.NotOwner):
            return await ctx.send(f"{emotes.cross} **Only bot owners can use this command.**")


def setup(bot):
    bot.add_cog(error(bot))
