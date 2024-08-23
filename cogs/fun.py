import sys
from random import randint

import discord
from discord.ext import commands

sys.path.append("..")
from main import BOT_PREFIX


class FunCog(commands.Cog):
    """ Модуль, содержащий веселые комадны бота. """
    def __init__(self, bot):
        self.boter = bot
        print(f"Module FunCog is loaded!")


    @commands.command()
    async def rand(self, ctx, x_min = 1, x_max = 100):
        if x_min >= x_max:
            emb1 = discord.Embed(title="Ошибка", description=f"Минимальное число должно быть меньше максимального (Xmin < Xmax).\nПомощь: `{BOT_PREFIX}help rand`", color=0xffffff)
        else:
            emb1 = discord.Embed(title="Выпало число...", description=f"Диапозон от {x_min} до {x_max}.\nВыпало число: ```{randint(x_min, x_max)}```", color=0xffffff)
        await ctx.send(embed = emb1)

    @commands.command()
    async def coin(self, ctx):
        r = randint(1, 2)
        if r == 1:
            emb1 = discord.Embed(title="Выпало...", description=f"Выпал **ОРЕЛ**", color=0xffffff)
        else:
            emb1 = discord.Embed(title="Выпало...", description=f"Выпала **РЕШКА**", color=0xffffff)
        await ctx.send(embed = emb1)


    
async def setup(bot):
    await bot.add_cog(FunCog(bot))