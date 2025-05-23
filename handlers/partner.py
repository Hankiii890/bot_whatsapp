# handlers/partner.py
from bot import bot
from whatsapp_chatbot_python import Notification

@bot.router.message(text_message=["Партнёрка", "2", "🤝 Партнёрка"])
def partner_handler(notification: Notification) -> None:
    notification.answer(
        "🤝 Партнёрская программа:\n\n"
        "Приглашайте друзей и получайте 20% от их платежей!\n\n"
        "Ваша реферальная ссылка: https://example.com/ref/12345\n"
        "Приглашено пользователей: 5\n"
        "Заработано: 50$\n\n"
        "Для выплаты выберите пункт «💰 Выплата» в меню."
    )