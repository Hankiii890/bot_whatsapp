# handlers/language.py
from bot import bot
from whatsapp_chatbot_python import Notification


@bot.router.message(command="to")
def language_handler(notification: Notification) -> None:
    command_parts = notification.event["messageData"]["textMessageData"]["textMessage"].split()
    if len(command_parts) < 2:
        notification.answer("Пожалуйста, укажите код языка, например: /to ru")
        return

    lang = command_parts[1].lower()
    if lang in ("en", "ru", "zh"):
        notification.answer(f"Язык изменён на {lang}. Для возврата в меню отправьте /start")
        # Здесь можно сохранить выбор языка в БД
    else:
        notification.answer("Неизвестный язык. Доступные варианты: en, ru, zh")