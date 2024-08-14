from discord.ext import commands
import discord


class GeneralCog(commands.Cog):
    """ Модуль, содержащий основные команды бота. """
    def __init__(self, bot):
        self.bot = bot
        print(f"Module {self.__class__.__name__} is loaded")


    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog loaded")

    
async def setup(bot):
    await bot.add_cog(GeneralCog(bot))