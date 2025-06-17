import os
from telegram import Bot
from telegram.error import TelegramError

# Carica le variabili d'ambiente
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@OcchioalP"  # Assicurati che sia scritto correttamente

# Inizializza il bot
bot = Bot(token=BOT_TOKEN)

# Test di pubblicazione
try:
    bot.send_message(chat_id=CHANNEL_ID, text="✅ Il bot è collegato correttamente al canale.")
    print("✅ Messaggio inviato correttamente.")
except TelegramError as e:
    print(f"❌ Errore Telegram: {e}")


