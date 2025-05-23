# handlers/pair.py
import re

@bot.router.message(regexp=r"^/to\s+([a-z]{2})$")
def pair_handler(notification: Notification):
    chat_id = notification.event["senderData"]["chatId"]
    lang = re.match(r"^/to\s+([a-z]{2})$", notification.event["messageData"]["textMessageData"]["textMessage"]).group(1)
    if lang not in SUPPORTED_PAIRS:
        return notification.answer(t("unsupported_pair", user.ui_lang))
    update_user_state(chat_id, lang=lang)
    notification.answer(t("pair_saved", user.ui_lang))
