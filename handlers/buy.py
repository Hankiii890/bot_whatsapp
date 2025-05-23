# handlers/buy.py
from bot import bot
from whatsapp_chatbot_python import Notification


@bot.router.message(text_message=["Купить подписку", "1"])
def buy_handler(notification: Notification) -> None:
    notification.answer(
        "Выберите тип подписки:\n\n"
        "1. Месячная подписка - 10$\n"
        "2. Годовая подписка - 100$\n"
        "3. Пожизненная подписка - 500$\n\n"
        "Отправьте номер выбранного варианта."
    )


@bot.router.message(text_message=["1", "2", "3"])
def subscription_type_handler(notification: Notification) -> None:
    choice = notification.event["messageData"]["textMessageData"]["textMessage"].strip()

    if choice == "1":
        notification.answer("Ссылка для оплаты месячной подписки: [ссылка]")
    elif choice == "2":
        notification.answer("Ссылка для оплаты годовой подписки: [ссылка]")
    elif choice == "3":
        notification.answer("Ссылка для оплаты пожизненной подписки: [ссылка]")