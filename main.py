import os

from dotenv import load_dotenv
import discord
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv("TOKEN")
BOTNAME = os.getenv("BOTNAME")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")


@bot.command()
async def ping(ctx):
    await ctx.reply("Pong!")

@bot.event
async def on_ready():
    print(f"\nБот {BOTNAME} запустился!\n")


bot.run(TOKEN)