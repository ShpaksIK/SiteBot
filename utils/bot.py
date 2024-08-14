import sys
import os

import discord
from discord.ext import commands

from events import Events


class Bot:
    def __init__(self, bot_name, bot_prefix):
        """ Инициализация бота """
        global bot, events

        self.bot_name = bot_name
        self.bot_prefix = bot_prefix

        intents = discord.Intents.all()
        bot = commands.Bot(command_prefix=bot_prefix, intents=intents)
        bot.remove_command("help")

        event = events.Events(bot_data=bot)

    def run_bot(self, token):
        """ Запуск бота по токену """
        bot.run(token)

    # def run_events(self):
    #     """ Запуск событий бота """
    #     events = Events(bot_data=bot)

    def run_commands(self): ...
