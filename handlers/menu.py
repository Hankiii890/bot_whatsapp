# handlers/menu.py
from bot import bot
from whatsapp_chatbot_python import Notification

@bot.router.message(text_message=[
    "1", "Купить подписку",
    "2", "🤝 Партнёрка",
    "3", "💰 Выплата",
    "4", "📊 Статистика",
    "5", "🌐 Сменить язык",
    "6", "🈂️ Языки",
])
def menu_handler(notification: Notification) -> None:
    choice = notification.event["messageData"]["textMessageData"]["textMessage"].strip()

    if choice in ("1", "Купить подписку"):
        notification.answer("Вы выбрали «Купить подписку». Готовлю ссылку на оплату…")
        # здесь ваш код buy.py
    elif choice in ("2", "🤝 Партнёрка"):
        notification.answer("Информация по партнёрке: …")
        # handlers.partner.py
    elif choice in ("3", "💰 Выплата"):
        notification.answer("Пожалуйста, введите сумму для выплаты.")
        # handlers.withdraw.py
    elif choice in ("4", "📊 Статистика"):
        notification.answer("Ваша статистика: …")
        # handlers.stats.py
    elif choice in ("5", "🌐 Сменить язык"):
        notification.answer("Отправьте /to <код>, например `/to ru`.")
        # reuse existing language_handler
    elif choice in ("6", "🈂️ Языки"):
        notification.answer("Доступные языки: en, ru, zh.")
    else:
        notification.answer("Не удалось распознать выбор, выберите пункт из меню.")