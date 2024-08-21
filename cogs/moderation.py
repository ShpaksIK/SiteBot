from discord.ext import commands


class ModerationCog(commands.Cog):
    """ Модуль, содержащий команды для управления сервером. """
    def __init__(self, bot):
        self.bot = bot
        print(f"Module ModerationCog is loaded!")


    @commands.command()
    async def moder(self, ctx):
        await ctx.send("moder")

    
async def setup(bot):
    await bot.add_cog(ModerationCog(bot))