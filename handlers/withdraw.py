# handlers/withdraw.py
from bot import bot
from whatsapp_chatbot_python import Notification


@bot.router.message(text_message=["Выплата", "3", "💰 Выплата"])
def withdraw_handler(notification: Notification) -> None:
    notification.answer(
        "💰 Выплата средств:\n\n"
        "Доступно для вывода: 100$\n"
        "Минимальная сумма выплаты: 10$\n\n"
        "Пожалуйста, введите сумму для выплаты."
    )


@bot.router.message()
def withdraw_amount_handler(notification: Notification) -> None:
    amount = notification.event["messageData"]["textMessageData"]["textMessage"].strip()

    try:
        amount = float(amount)
        if amount < 10:
            notification.answer("Минимальная сумма выплаты - 10$.")
        else:
            notification.answer(f"Запрос на выплату {amount}$ принят. Ожидайте перевод в течение 24 часов.")
    except ValueError:
        notification.answer("Пожалуйста, введите корректную сумму (например: 50 или 50.5).")