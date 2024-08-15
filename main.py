import os
import asyncio

from dotenv import load_dotenv
import discord
from discord.ext import commands


# Получение данных .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
BOTNAME = os.getenv("BOTNAME")
BOTPREFIX = os.getenv("BOTPREFIX")

# Инициализация бота
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=BOTPREFIX, intents=intents, help_command=None)

async def load_extensions():
    # Инициализация модулей
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    # Запуск бота
    await load_extensions()
    await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())