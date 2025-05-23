# handlers/stats.py
from bot import bot
from whatsapp_chatbot_python import Notification

@bot.router.message(text_message=["Статистика", "4", "📊 Статистика"])
def stats_handler(notification: Notification) -> None:
    # Здесь можно добавить логику получения реальной статистики из БД
    notification.answer(
        "📊 Ваша статистика:\n\n"
        "Подписка активна до: 2023-12-31\n"
        "Использовано трафика: 75%\n"
        "Рефералов: 5\n"
        "Заработано: 50$\n\n"
        "Для возврата в меню отправьте /start"
    )