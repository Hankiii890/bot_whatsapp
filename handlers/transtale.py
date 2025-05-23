# handlers/translate.py
from services.translator import translate_text

@bot.router.message(text_message=None)
def translate_handler(notification: Notification):
    chat_id = notification.event["senderData"]["chatId"]
    user = get_or_create_user(chat_id)
    # если мы в режиме ожидания payout — пропускаем
    if user.state == "awaiting_payout":
        return
    txt = notification.event["messageData"]["textMessageData"]["textMessage"]
    tr = translate_text(txt, source="auto", target=user.lang)
    notification.answer(f"{t('translation', user.ui_lang)}: {tr}")
