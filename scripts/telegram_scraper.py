
import os
import json
import datetime
from telethon.sync import TelegramClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")


channels = [
    "https://t.me/lobelia4cosmetics",
    "https://t.me/tikvahpharma"
]

# Today's date for the folder structure
today = datetime.date.today().isoformat()

# Where we'll save messages
base_path = f"data/raw/telegram_messages/{today}"
os.makedirs(base_path, exist_ok=True)

# Start Telegram client
with TelegramClient("anon", api_id, api_hash) as client:
    for link in channels:
        try:
            channel = client.get_entity(link)
            messages = []
            for msg in client.iter_messages(channel, limit=100):
                messages.append(msg.to_dict())

            # Save to JSON
            channel_name = link.split("/")[-1]
            with open(f"{base_path}/{channel_name}.json", "w", encoding="utf-8") as f:
                json.dump(messages, f, ensure_ascii=False, indent=2)

            print(f"  Scraped: {channel_name}")
        except Exception as e:
            print(f" Error scraping {link}: {e}")
