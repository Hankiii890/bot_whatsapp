# bot.py
from whatsapp_chatbot_python import GreenAPIBot
import config

bot = GreenAPIBot(
    config.INSTANCE_ID,
    config.API_TOKEN
)
