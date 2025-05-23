# handlers/payout_details.py
@bot.router.message(text_message=None)
def payout_details_handler(notification: Notification):
    chat_id = notification.event["senderData"]["chatId"]
    user = get_or_create_user(chat_id)
    if user.state != "awaiting_payout":
        return
    # парсим «телефон, банк»
    phone, bank = map(str.strip, notification.event["messageData"]["textMessageData"]["textMessage"].split(",",1))
    # создаём PayoutRequest
    with SessionLocal() as s:
        req = PayoutRequest(user_id=chat_id, phone=phone, bank=bank, amount=user.balance)
        s.add(req); s.commit()
    update_user_state(chat_id, state="idle")
    notification.answer(t("payout_created", user.ui_lang))
