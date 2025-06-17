import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")  # già configurato
CHANNEL_ID = "@Occhio_al_Prezzo"  # sostituisci con il tuo canale

bot = Bot(token=BOT_TOKEN)

bot.send_message(chat_id=CHANNEL_ID, text="✅ Il bot è collegato correttamente al canale.")

from telegram.error import TelegramError

try:
    bot.send_message(chat_id=CHANNEL_ID, text="✅ Test di pubblicazione.")
except TelegramError as e:
    print(f"Errore Telegram: {e}")

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Se previsto

