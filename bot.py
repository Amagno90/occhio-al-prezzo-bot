import os
import feedparser
import requests
from flask import Flask

app = Flask(__name__)

# CONFIGURAZIONE
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = '@occhioalprezzo'
AFFILIATE_ID = 'occhioalpre08-21'
RSS_FEED = 'https://www.amazon.it/gp/rss/bestsellers/electronics/'

@app.route('/')
def home():
    return "Bot attivo"

@app.route('/esegui')
def esegui():
    feed = feedparser.parse(RSS_FEED)
    messaggi_inviati = 0

    for entry in feed.entries[:5]:
        titolo = entry.title
        link = entry.link + f"?tag={AFFILIATE_ID}"
        messaggio = f"*{titolo}*\n{link}"

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHANNEL_ID,
            "text": messaggio,
            "parse_mode": "Markdown"
        }

        r = requests.post(url, data=payload)
        if r.status_code == 200:
            messaggi_inviati += 1

    return f"✅ {messaggi_inviati} messaggi inviati."
