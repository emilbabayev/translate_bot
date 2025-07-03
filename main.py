import asyncio
import nest_asyncio
from bot import TelegramBot


if __name__ == '__main__':
    """
    Старт работы в асинхронном режиме
    """
    nest_asyncio.apply()
    asyncio.run(TelegramBot().run())