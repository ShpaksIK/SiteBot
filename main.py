import os
import asyncio

from dotenv import load_dotenv
import discord
from discord.ext import commands

from db.database import Database


# Получение данных .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
BOT_PREFIX = os.getenv("BOT_PREFIX")
BOT_SITE = os.getenv("BOT_SITE")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Подключение к базе данных
db_con = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
db_con.create_connection()

# Инициализация бота
intents = discord.Intents().all()
intents.members = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents, help_command=None)

async def load_extensions():
    # Инициализация модулей
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    # Запуск бота
    await load_extensions()
    await bot.start(BOT_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())