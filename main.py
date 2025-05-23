# main.py
from bot import bot

# Подключаем все хэндлеры, чтобы они зарегистрировались в bot.router
import handlers.start
import handlers.language

if __name__ == "__main__":
    bot.run_forever()
