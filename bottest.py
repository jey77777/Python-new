import requests

TOKEN = "7597430865:AAGGzd112LAyKVnqoud0w6nidBFwYQAflCQ"
chat_id = "1022433753"  # Odatda sizning Telegram ID'ingiz
matn = input("Xabar jo'nating: ")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
params = {
    "chat_id": chat_id,
    "text": matn
}

javob = requests.get(url, params=params)
print(javob.json())