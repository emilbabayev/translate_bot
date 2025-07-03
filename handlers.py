from telegram import Update
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters
from translator import translate
from settings import LANGUAGES
from utils import get_language_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Приветствует пользователя и показывает кнопки, предлагая ему выбор языка для перевода.
    """
    if not context.user_data.get('started'):
        context.user_data['started'] = True
        await update.message.reply_text('Приветствую!\nВыберите язык перевода: ', reply_markup=get_language_keyboard())


async def set_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Показывает кнопки выбора языка для перевода.
    """
    await update.message.reply_text('Выберите язык перевода: ', reply_markup=get_language_keyboard())


async def get_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Показывает выбранный язык, если он выбран. Если не выбран, показывает соответствующее сообщение
    """
    curr_lang = context.user_data.get('lang')
    if curr_lang:
        current_lang_label = LANGUAGES[curr_lang]
        user_name = update.message.from_user.full_name
        message = f'Текущий язык {user_name}: {current_lang_label}'
    else:
        message = 'Язык не выбран'

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=message)


async def handle_lang_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Считывает нажатие на кнопку выбора языка и меняет текущий язык на выбранный.
    """
    query = update.callback_query
    await query.answer()
    selected_lang = query.data
    context.user_data["lang"] = selected_lang

    await context.bot.delete_message(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id
    )


async def reply_translated(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Переводит отправленный текст на выбранный язык и отправляет в чат.
    """
    user = update.message.from_user # имя отправителя
    user_text = update.message.text # сообщение отправителя
    lang = context.user_data.get("lang")  # язык перевода

    if lang:
        # удаляет сообщение пользователя (работает только в супергруппах, либо в самом чате с ботом)
        await update.message.delete()

        translated = await translate(user_text, lang) # переведенное сообщение

        await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=f'{user.full_name}: {translated}')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text='Язык не выбран')


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Завершает работу бота.
    """
    context.user_data.clear()
    await update.message.reply_text('Работа завершена. Введите /start для повторного запуска.')


def register_handlers(app):
    """
    Добавляет все хэндлеры для <app>
    """
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setlang", set_lang))
    app.add_handler(CommandHandler("info", get_info))
    app.add_handler(CommandHandler("end", end))
    app.add_handler(CallbackQueryHandler(handle_lang_choice))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_translated))