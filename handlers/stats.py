# handlers/stats.py
@bot.router.message(text_message=["4", t("btn_stats", "*")])
def stats_handler(notification: Notification):
    chat_id = notification.event["senderData"]["chatId"]
    with SessionLocal() as s:
        sent = s.query(Message).filter_by(user_id=chat_id).count()
        remain = sum(sub.message_limit-sub.messages_used
                     for sub in s.query(Subscription).filter_by(user_id=chat_id, active=True))
    notification.answer(
        f"{t('messages_sent', user.ui_lang)}: {sent}\n"
        f"{t('messages_left', user.ui_lang)}: {remain}"
    )
