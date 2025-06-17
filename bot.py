import os
import time
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)

def leggi_link():
    if not os.path.exists("links.txt"):
        return []
    with open("links.txt", "r") as file:
        return [line.strip() for line in file if line.strip()]

def salva_link(link_list):
    with open("links.txt", "w") as file:
        for link in link_list:
            file.write(link + "\n")

def pubblica_link():
    link_list = leggi_link()
    if not link_list:
        print("Nessun link da pubblicare.")
        return

    primo_link = link_list.pop(0)
    try:
        bot.send_message(chat_id=CHANNEL_ID, text=f"🔥 Offerta Amazon:\n{primo_link}")
        print(f"Inviato: {primo_link}")
    except Exception as e:
        print(f"Errore durante l'invio: {e}")
        # se vuoi rimettere il link in caso di errore, decomenta la riga sotto:
        # link_list.insert(0, primo_link)

    salva_link(link_list)

# Pubblica ogni 60 secondi (modifica a piacere)
if __name__ == "__main__":
    while True:
        pubblica_link()
        time.sleep(60)

