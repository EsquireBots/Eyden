from discord.ext import commands
from utils.help import PenguinHelp

class HelpCog(commands.Cog, name="Utility"):
    def __init__(self, bot):
        self.bot = bot
        bot.help_command = PenguinHelp()
        bot.help_command.cog = self
        self.help_icon = 'ℹ'

def setup(bot):
    bot.add_cog(HelpCog(bot))