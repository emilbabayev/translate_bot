from telegram import BotCommand
from dotenv import load_dotenv
import os


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")


LANGUAGES = {
    'EN': 'English🇬🇧',
    'FR': 'French🇫🇷',
    'ES': 'Spanish🇪🇸',
    'IT': 'Italian🇮🇹',
    'AR': 'Arabic🇦🇪',
    'JA': 'Japanese🇯🇵'
}
""" Все доступные языки перевода. Ключ - код для DeepL, значение - подпись языка(label). """


COMMANDS = [
        BotCommand("start", "Начать работу"),
        BotCommand("setlang", "Выбрать язык"),
        BotCommand("info", "Показать текущий язык"),
        BotCommand("end", 'Завершить работу бота')
]
""" Список команд бота, появляющийся при вводе '/' """