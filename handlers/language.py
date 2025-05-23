# handlers/language.py
from bot import bot
from whatsapp_chatbot_python import Notification
from services.db import get_or_create_user, update_user_state
from services.i18n import t
import re


@bot.router.message(regexp=r"^/to\s+(en|ru|zh)$")
def language_handler(notification: Notification):
    chat_id = notification.event["senderData"]["chatId"]
    text = notification.event["messageData"]["textMessageData"]["textMessage"]

    match = re.match(r"^/to\s+(en|ru|zh)$", text)
    if not match:
        return
    lang = match.group(1)

    user = get_or_create_user(chat_id)
    update_user_state(chat_id, state="idle", lang=lang)
    notification.answer(t(lang, "pair_saved"))
