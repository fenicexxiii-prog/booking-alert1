import requests
import time

URL = "https://www.booking.com/hotel/it/primaverammare.it.html"

BOT_TOKEN = https://api.telegram.org/bot8998464103:AAESkI9kP3w-PKwVD9vaEqjNJ_014PQRksM/sendMessage?chat_id=7985695301&text=Test%20OK
CHAT_ID = "7985695301"

last_state = None

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

while True:
    try:
        r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
        text = r.text

        if last_state and text != last_state:
            send("⭐ Possibile nuova recensione su Booking!")

        last_state = text

        time.sleep(3600)

    except Exception as e:
        send(f"Errore script: {e}")
        time.sleep(3600)
