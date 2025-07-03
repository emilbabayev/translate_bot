from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from settings import LANGUAGES


def get_language_keyboard():
    """
    Возвращает группу кнопок выбора языка для перевода.
    """
    buttons = [InlineKeyboardButton(label, callback_data=code) for code, label in LANGUAGES.items()]
    return InlineKeyboardMarkup([buttons[:3], buttons[3:]])