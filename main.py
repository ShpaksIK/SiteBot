import os
import asyncio

from dotenv import load_dotenv
import discord
from discord.ext import commands


async def main():
    # Получение данных .env
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    BOTNAME = os.getenv("BOTNAME")
    BOTPREFIX = os.getenv("BOTPREFIX")

    # Инициализация бота
    intents = discord.Intents().all()
    bot = commands.Bot(command_prefix=BOTPREFIX, intents=intents)

    # Инициализация модулей
    async def load_extensions():
        for filename in os.listdir("./utils/cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"cogs.{filename[:-3]}")

    # Запуск бота
    # bot.run(TOKEN)
    # async with bot:
    #     await load_extensions()
    await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())