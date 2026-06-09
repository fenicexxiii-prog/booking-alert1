import requests

URL = "https://www.booking.com/hotel/it/primaverammare.it.html"

BOT_TOKEN = "INSERISCI_TOKEN"
CHAT_ID = "7985695301"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot=8998464103:AAESkI9kP3w-PKwVD9vaEqjNJ_014PQRksM/sendMessage?chat_id=7985695301&text=Test%20OK/sendMessage",
        data={"chat_id": CHAT_ID,7985695301: msg}
    )

def check():
    r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    if "review" in r.text.lower():
        send("⭐ Test Booking monitor attivo")

check()
