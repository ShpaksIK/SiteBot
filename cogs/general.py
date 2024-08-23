import sys

import discord
from discord.ext import commands

sys.path.append("..")
from main import BOT_PREFIX, BOT_SITE, BOT_NAME, db_con
from utils.math import calculate_server_age
from utils.check import check_status


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
        emb1.add_field(name="Участники", value=f"Всего: **{total_members}**\nЛюдей: **{total_members-total_bots}**\nБотов: **{total_bots}**")
        emb1.add_field(name="Каналы", value=f"Всего: **{total_channels}**\nТекстовые: **{text_channels}**\nГолосовые: **{voice_channels}**")
        emb1.add_field(name="Дата создания", value=f"{creation_date_str}\n*{server_age_str}*")
        emb1.add_field(name="Администраторы", value=f"Владелец: **{owner}**\nАдминистраторов: **{admin_members}**")
        emb1.set_thumbnail(url=server_avatar)
        emb1.set_footer(text=f"ID: {server_id}")
        await ctx.send(embed = emb1)

    @commands.command()
    async def user(self, ctx, user_id: discord.Member = None):
        if user_id is None:
            user_id = ctx.author
        days_of_week = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}
        months = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
        ampm = "утра" if user_id.created_at.strftime('%p') == "AM" else "вечера"
        formatted_date = user_id.created_at.strftime("%a, %#d %B %Y года, %I:%M %p")
        formatted_date = formatted_date.replace(user_id.created_at.strftime('%a'), days_of_week[user_id.created_at.weekday()])
        formatted_date = formatted_date.replace(user_id.created_at.strftime('%B'), months[user_id.created_at.month])
        formatted_date = formatted_date.replace(user_id.created_at.strftime('%p'), ampm)
        user_status = check_status(discord, user_id)
        roles = [role.id for role in user_id.roles if role.name != '@everyone']
        roles_list = ', '.join(f"<@&{role_id}>" for role_id in roles)
        join_time = user_id.joined_at.strftime("%Y.%m.%d в %H:%M:%S")

        emb1 = discord.Embed(title="Информация о пользователе", color=0xffffff)
        emb1.add_field(name="**Ник**", value=f"<@{user_id.id}> | `{user_id.name}`", inline=True)
        emb1.add_field(name="**Активность**", value=f"{user_status}",inline=True)
        emb1.add_field(name="**Акаунт был создан**", value=f'{formatted_date}', inline=False)
        emb1.add_field(name="**Присоединился**", value=f"{join_time}", inline=False)
        emb1.add_field(name="**Роли пользователя**", value=f"{roles_list}", inline=False)
        emb1.set_thumbnail(url=user_id.avatar)
        emb1.set_footer(text=f"ID: {user_id.id}")
        await ctx.reply(embed = emb1)
    

async def setup(bot):
    await bot.add_cog(GeneralCog(bot))
