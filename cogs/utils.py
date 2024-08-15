from discord.ext import commands


class UtilCog(commands.Cog):
    """ Модуль, содержащий утилиты бота. """
    def __init__(self, bot):
        self.bot = bot
        print(f"Module UtilCog is loaded!")


    @commands.command()
    async def util(self, ctx):
        await ctx.send("util")

    
async def setup(bot):
    await bot.add_cog(UtilCog(bot))