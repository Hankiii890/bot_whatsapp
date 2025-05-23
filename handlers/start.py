# handlers/start.py
from bot import bot
from whatsapp_chatbot_python import Notification


@bot.router.message(command="start")
def start_handler(notification: Notification) -> None:
    sender = notification.event["senderData"]
    name = sender.get("senderName", "")  # имя пользователя

    # Текстовое меню
    notification.answer(
        (
            f"Привет, {name}!\n\n"
            "Что вы хотите сделать?\n\n"
            "1. Купить подписку\n"
            "2. 🤝 Партнёрка\n"
            "3. 💰 Выплата\n"
            "4. 📊 Статистика\n"
            "5. 🌐 Сменить язык\n"
            "6. 🈂️ Языки\n\n"
            "Отправьте цифру или полное название пункта."
        )
    )
