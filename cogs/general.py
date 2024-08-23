import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta

import discord
from discord.ext import commands

sys.path.append("..")
from main import BOT_PREFIX, BOT_SITE, BOT_NAME, db_con
from utils.math import calculate_server_age


class GeneralCog(commands.Cog):
    """ Модуль, содержащий основные команды бота. """
    def __init__(self, bot):
        self.boter = bot
        print(f"Module GeneralCog is loaded!")


    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def help(self, ctx, command_name = None):
        if command_name is None:
            bot_commands = db_con.get_commands(db_con.connection)
            bot_commands_general = ""
            for i in bot_commands:
                bot_commands_general += BOT_PREFIX + i[1] + "\n" if i[0] == "general" else ""
            bot_commands_moderation = ""
            for i in bot_commands:
                bot_commands_moderation += BOT_PREFIX + i[1] + "\n" if i[0] == "moderation" else ""
            bot_commands_fun = ""
            for i in bot_commands:
                bot_commands_fun += BOT_PREFIX + i[1] + "\n" if i[0] == "fun" else ""
            bot_commands_music = ""
            for i in bot_commands:
                bot_commands_music += BOT_PREFIX + i[1] + "\n" if i[0] == "music" else ""
            bot_commands_utils = ""
            for i in bot_commands:
                bot_commands_utils += BOT_PREFIX + i[1] + "\n" if i[0] == "utils" else ""

            emb1 = discord.Embed(title="Информация о командах", color=0xffffff)
            emb1.add_field(name = f"", value=f"Перед использованием команды ставьте префикс: `{BOT_PREFIX}`", inline=False)
            emb1.add_field(name = f"", value=f"Для подробной информации о команде используйте: `{BOT_PREFIX}help [command]`", inline=False)
            emb1.add_field(name = f"Модерирование", value=f"```{bot_commands_moderation}```", inline=True)
            emb1.add_field(name = f"Музыка", value=f"```{bot_commands_music}```", inline=True)
            emb1.add_field(name = f"", value=f"", inline=False)
            emb1.add_field(name = f"Общие", value=f"```{bot_commands_general}```", inline=True)
            emb1.add_field(name = f"Утилиты", value=f"```{bot_commands_utils}```", inline=True)
            emb1.add_field(name = f"Развлечение", value=f"```{bot_commands_fun}```", inline=True)
            emb1.add_field(name = f"", value=f"Ещё больше информации о командах вы можете найти на сайте бота: {BOT_SITE}commands", inline=False)
            await ctx.send(embed = emb1)
        
        else:
            bot_command = db_con.get_commands(db_con.connection, command=command_name)
            print(bot_command)
            if bot_command == []:
                emb1 = discord.Embed(title="Ошибка", description="Такой команды не существует.", color=0xffffff)
            else:
                bot_command = bot_command[0]
                emb1 = discord.Embed(title=f"Команда {bot_command[2]}", color=0xffffff)
                emb1.add_field(name = f"Описание", value=f"```{bot_command[3]}```", inline=False)
                emb1.add_field(name = f"Использование", value=f"```{bot_command[4]}```", inline=False)
                emb1.add_field(name = f"", value=f"", inline=False)
                emb1.add_field(name = f"", value=f"Ещё больше информации о командах вы можете найти на сайте бота: {BOT_SITE}commands", inline=False)
            await ctx.send(embed = emb1)

    @commands.command()
    async def bot(self, ctx):
        joined_date = self.boter.get_guild(1176528473112711229).get_member(self.boter.user.id).joined_at.strftime('%d.%m.%Y, %H:%M')
        emb1 = discord.Embed(title=f"Информация о {BOT_NAME}", color=0xffffff)
        emb1.add_field(name="Ник", value=f"<@{self.boter.user.id}> | `{self.boter.user.name}`", inline=True)
        emb1.add_field(name="Айди", value=f"`{self.boter.user.id}`", inline=True)
        emb1.add_field(name="Префикс", value=f"`{BOT_PREFIX}`", inline=True)
        emb1.add_field(name="Бот был создан", value=f'{self.boter.user.created_at.strftime("%d.%m.%Y, %H:%M")}', inline=True)
        emb1.add_field(name="Присоединился к серверу", value=f'{joined_date}', inline=True)
        emb1.add_field(name = f"Ссылки", value=f"[Сайт бота](http://localhost:3000/)\n[Панель управления](http://localhost:3000/servers)", inline=False)
        emb1.add_field(name = f"", value=f"Ыыыыыы наш бот очень крутооой ыываыаыаыаы!!!!", inline=False)
        emb1.set_thumbnail(url=self.boter.user.avatar)
        await ctx.send(embed = emb1)

    @commands.command()
    async def server(self, ctx):
        guild = ctx.guild
        server_name = guild.name
        server_id = guild.id
        owner = guild.owner
        admin_members = len([member for member in guild.members if member.guild_permissions.administrator])
        creation_date = guild.created_at
        creation_date_str = creation_date.strftime("%Y-%m-%d")
        years, months, days = calculate_server_age(creation_date)
        server_age_str = f"{years} лет, {months} месяцев, {days} дней"
        total_members = guild.member_count
        total_bots = len([member for member in guild.members if member.bot])
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        total_channels = text_channels + voice_channels
        server_avatar = guild.icon.url if guild.icon else 'Нет аватара'

        emb1 = discord.Embed(title=f"Информация о сервере {server_name}", color=0xffffff)
        emb1.set_thumbnail(url=server_avatar)
        emb1.add_field(name="Участники", value=f"Всего: **{total_members}**\nЛюдей: **{total_members-total_bots}**\nБотов: **{total_bots}**")
        emb1.add_field(name="Каналы", value=f"Всего: **{total_channels}**\nТекстовые: **{text_channels}**\nГолосовые: **{voice_channels}**")
        emb1.add_field(name="Дата создания", value=f"{creation_date_str}\n*{server_age_str}*")
        emb1.add_field(name="Администраторы", value=f"Владелец: **{owner}**\nАдминистраторов: **{admin_members}**")
        emb1.set_footer(text=f"ID: {server_id}")
        await ctx.send(embed=emb1)

    @commands.command()
    async def user(self, ctx):
        pass
    

async def setup(bot):
    await bot.add_cog(GeneralCog(bot))
