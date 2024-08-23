import discord
from discord.ext import commands
from translate import Translator


class UtilCog(commands.Cog):
    """ Модуль, содержащий утилиты бота. """
    def __init__(self, bot):
        self.boter = bot
        print(f"Module UtilCog is loaded!")


    @commands.command()
    async def avatar(self, ctx, user_id: discord.Member = None):
        if user_id is None:
            user_id = ctx.author
        avatar_url = user_id.avatar
        emb1 = discord.Embed(title=f"Аватар {user_id.name}", description=f"[Нажмите, чтобы скачать аватар]({avatar_url})", color=0xffffff)
        emb1.set_image(url=avatar_url)
        await ctx.send(embed = emb1)

    @commands.command()
    async def tr(self, ctx, *text):
        translator = Translator(from_lang="english", to_lang="russian")
        t = " ".join(text)
        translation = translator.translate(t)

        emb1 = discord.Embed(title=f"Перевод с RU в ENG", description=f"{translation}", color=0xffffff)
        await ctx.send(embed = emb1)

    
async def setup(bot):
    await bot.add_cog(UtilCog(bot))