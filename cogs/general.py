from discord.ext import commands


class GeneralCog(commands.Cog):
    """ Модуль, содержащий основные команды бота. """
    def __init__(self, bot):
        self.bot = bot
        print(f"Module GeneralCog is loaded!")


    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")

    
async def setup(bot):
    await bot.add_cog(GeneralCog(bot))