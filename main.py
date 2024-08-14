import os

from dotenv import load_dotenv

from src.bot import Bot


def main():
    # Получение данных .env
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    BOTNAME = os.getenv("BOTNAME")
    BOTPREFIX = os.getenv("BOTPREFIX")

    # Создание экземпляра класса Bot
    global bot_main
    bot_main = Bot(bot_name=BOTNAME, bot_prefix=BOTPREFIX)
    bot_main.run_bot(TOKEN)


if __name__ == "__main__":
    main()