class Events:
    """ Инициализация событий """
    def __init__(self, bot_data):
        global bot

        self.bot = bot_data
        

    @bot.command()
    async def ping(ctx):
        await ctx.reply("Pong!")

    @bot.event
    async def on_ready():
        print(f"\nБот запустился!\n")