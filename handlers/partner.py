# handlers/partner.py
from bot import bot
from whatsapp_chatbot_python import Notification
from services.db import SessionLocal
from utils import get_refferal_counts_by_period, get_referral_counts
from services.i18n import t

@bot.router.message(text_message=["2", t("btn_partner", "*")])
def partner_handler(notification: Notification):
    chat_id = notification.event["senderData"]["chatId"]
    with SessionLocal() as s:
        user = s.query(User).filter_by(telegram_id=chat_id).one()
        lvl1, lvl2 = get_referral_counts(user.telegram_id)
        today = get_refferal_counts_by_period(user.telegram_id, 1)
        month = get_refferal_counts_by_period(user.telegram_id, 30)
    reply = "\n".join([
        f"{t('ref_link', user.ui_lang)}: https://wa.me/.../?start={chat_id}",
        f"{t('partners_lvl1', user.ui_lang)}: {lvl1}",
        f"{t('partners_lvl2', user.ui_lang)}: {lvl2}",
        f"{t('invited_today', user.ui_lang)}: {today}",
        f"{t('invited_month', user.ui_lang)}: {month}",
    ])
    notification.answer(reply)
