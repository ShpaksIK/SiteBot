from discord.ext import commands


class MusicCog(commands.Cog):
    """ Модуль, содержащий команды для управления музыки. """
    def __init__(self, bot):
        self.bot = bot
        print(f"Module MusicCog is loaded!")


    @commands.command()
    async def music(self, ctx):
        await ctx.send("music")

    
async def setup(bot):
    await bot.add_cog(MusicCog(bot))