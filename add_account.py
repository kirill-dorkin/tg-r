import asyncio
import json
from pathlib import Path

from pyrogram import Client

from config import CHANNELS
from reactionbot import is_subscribed, react_to_unreacted_messages

WORK_DIR = Path(__file__).parent.joinpath("sessions")
API_CONFIG = Path(__file__).parent.joinpath("api_config.json")

async def main():
    phone = input("Phone number: ")
    if API_CONFIG.exists():
        try:
            with open(API_CONFIG) as f:
                data = json.load(f)
            api_id = int(data["api_id"])
            api_hash = data["api_hash"]
        except Exception:
            api_id = int(input("API ID: "))
            api_hash = input("API HASH: ")
            with open(API_CONFIG, "w") as f:
                json.dump({"api_id": api_id, "api_hash": api_hash}, f)
    else:
        api_id = int(input("API ID: "))
        api_hash = input("API HASH: ")
        with open(API_CONFIG, "w") as f:
            json.dump({"api_id": api_id, "api_hash": api_hash}, f)

    WORK_DIR.mkdir(exist_ok=True)
    app = Client(phone, api_id=api_id, api_hash=api_hash, workdir=WORK_DIR.as_posix())
    print("Authorize this account using the received code...")
    await app.start()
    for channel in CHANNELS:
        subscribed = await is_subscribed(app, channel)
        if not subscribed:
            await app.join_chat(channel)
        await react_to_unreacted_messages(app, channel)
    await app.stop()

    config_path = WORK_DIR.joinpath(f"{phone}.json")
    with open(config_path, "w") as f:
        json.dump({"api_id": api_id, "api_hash": api_hash, "phone_number": phone}, f)

    print("Account added successfully")

if __name__ == "__main__":
    asyncio.run(main())
