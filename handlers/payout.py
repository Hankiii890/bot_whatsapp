# handlers/payout.py
from bot import bot
from whatsapp_chatbot_python import Notification
from services.db import SessionLocal
from utils import check_and_deduct_limit
from services.i18n import t

@bot.router.message(text_message=["3", t("btn_payout", "*")])
def payout_request_handler(notification: Notification):
    chat_id = notification.event["senderData"]["chatId"]
    # проверяем баланс
    with SessionLocal() as s:
        bal = s.query(func.coalesce(func.sum(Commission.amount), 0))\
               .filter(Commission.receiver_id==chat_id, Commission.is_paid.is_(False))\
               .scalar()
    if bal < MIN_PAYOUT_AMOUNT:
        return notification.answer(t("min_payout", user.ui_lang).format(amount=MIN_PAYOUT_AMOUNT))
    # перевод в «режим ожидания ввода реквизитов»
    update_user_state(chat_id, state="awaiting_payout")
    notification.answer(t("enter_payout_details", user.ui_lang))
