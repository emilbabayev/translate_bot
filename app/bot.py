from telegram.ext import ApplicationBuilder
from handlers import register_handlers
from settings import TOKEN, COMMANDS


class TelegramBot:
    """
    Бот, переводящий сообщения пользователя на выбранный язык.
    """
    def __init__(self) -> None:
        """
        Инициализация бота по TOKEN
        """
        self.app = ApplicationBuilder().token(TOKEN).build()

    async def set_bot_commands(self) -> None:
        """
        Запускает команды бота
        :return:
        """
        await self.app.bot.set_my_commands(COMMANDS)

    async def run(self) -> None:
        """
        Запуск работы бота
        :return:
        """
        await self.set_bot_commands()
        register_handlers(self.app)
        await self.app.run_polling()