from google_sheets.celery import app
import telebot
from django.conf import settings

# TOKEN: '5603456251:AAER2H_ALwag2opjfE9yN2lJSRTiA5VhgIU' stored in settings.TELEGRAM_BOT_TOKEN
# CHAT ID: 5218003772 stored in settings.TELEGRAM_CHAT_ID


@app.task
def msg_to_telegram(message):
    bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
    bot.send_message(settings.TELEGRAM_CHAT_ID, message)

