import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")  # già configurato
CHANNEL_ID = "@OcchioalP"  # sostituisci con il tuo canale

bot = Bot(token=BOT_TOKEN)

bot.send_message(chat_id=CHANNEL_ID, text="✅ Il bot è collegato correttamente al canale.")
