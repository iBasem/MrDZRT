import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from telegram.ext import Updater

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '6744267308:AAGWAP0f-pVrQUub-W5rZdU-ZVgWOVRxyG8'
# Replace 'YOUR_CHAT_ID' with your actual chat ID
CHAT_ID = '929510251'
URL = 'https://www.dzrt.com/en/icy-rush.html'
KEYWORD = 'Back In Stock On Wednesday'

def check_availability():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            if KEYWORD in soup.get_text():
                message = f"متوفر حاليا - {datetime.now()}"
                print(f"[{datetime.now()}] Product is available!")
                send_message(message)
            else:
                print(f"[{datetime.now()}] Product is not available.")
        else:
            print(f"[{datetime.now()}] Error: Unable to fetch page.")
    except Exception as e:
        print(f"[{datetime.now()}] Error occurred: {e}")

def send_message(message):
    updater = Updater(TOKEN, use_context=True)
    updater.bot.send_message(chat_id=CHAT_ID, text=message)

def main():
    while True:
        check_availability()
        time.sleep(120)  # Check every 2 minutes

if __name__ == '__main__':
    main()
