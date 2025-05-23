# main.py
from bot import bot

# Подключаем все хэндлеры
import handlers.start
import handlers.menu
import handlers.buy
import handlers.partner
import handlers.withdraw
import handlers.stats
import handlers.language

if __name__ == "__main__":
    bot.run_forever()