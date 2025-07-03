from telegram import BotCommand
import os


TOKEN = '7803134190:AAHT9RQ6KEs1dztLik_7Kk2G7A1Gui6FfCM'   # Токен созданного telegram-бота
DEEPL_API_KEY = "afe361de-5310-461b-bba9-43459a26ffd5:fx"  # Токен DeepL API переводчика


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