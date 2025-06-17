import os
import asyncio
from telegram import Bot
from telegram.error import TelegramError
from dotenv import load_dotenv

# Carica variabili da .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@OcchioalP"  # Puoi sostituirlo con l'ID numerico del canale, se lo conosci

bot = Bot(token=BOT_TOKEN)

async def main():
    try:
        await bot.send_message(chat_id=CHANNEL_ID, text="✅ Il bot è collegato correttamente al canale.")
        print("✅ Messaggio inviato correttamente.")
    except TelegramError as e:
        print(f"❌ Errore Telegram: {e}")

if __name__ == "__main__":
    asyncio.run(main())


