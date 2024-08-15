from discord.ext import commands


class FunCog(commands.Cog):
    """ Модуль, содержащий веселые комадны бота. """
    def __init__(self, bot):
        self.bot = bot
        print(f"Module FunCog is loaded!")


    @commands.command()
    async def fun(self, ctx):
        await ctx.send("fun")

    
async def setup(bot):
    await bot.add_cog(FunCog(bot))