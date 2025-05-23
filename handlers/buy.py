# handlers/buy.py
from bot import bot
from whatsapp_chatbot_python import Notification
from services.db import SessionLocal
from utils import create_payment_link       # из вашего payment.py
from services.i18n import t

@bot.router.message(text_message=["1", t("btn_buy", "*")])
def buy_handler(notification: Notification):
    chat_id = notification.event["senderData"]["chatId"]
    # получаем юзера из БД
    with SessionLocal() as s:
        user = s.query(User).filter_by(telegram_id=chat_id).first()
        # …либо создаём, если нет
    # генерируем ссылку на оплату (тот же код, что в Telegram-скрипте)
    link = create_payment_link(user.id, ...)

    notification.answer(
        t(user.ui_lang, "payment_link") + "\n" + link
    )
