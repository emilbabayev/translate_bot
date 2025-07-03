import aiohttp
from settings import DEEPL_API_KEY

async def translate(text: str, target_lang: str, source_lang: str = None) -> str:
    """
    Переводчик текста через DeepL API

    :param text: входной текст
    :param target_lang: язык, на который будет переводиться входной текст
    :param source_lang: язык входного текста
    :return: переведенное сообщение
    """
    url = "https://api-free.deepl.com/v2/translate"
    headers = {
        "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "text": text,
        "target_lang": target_lang.upper()
    }
    if source_lang is not None:
        data["source_lang"] = source_lang.upper()

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as resp:
            text_raw = await resp.text()
            print(text_raw)  # для отладки
            try:
                result = await resp.json()
                return result["translations"][0]["text"]
            except Exception:
                return f"Ошибка при переводе: {text_raw}"