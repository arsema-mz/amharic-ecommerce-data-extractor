from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import json

api_id = 28536612       
api_hash = '9da905b4322010cb5d0f733f80187c6f'  

client = TelegramClient('session_name', api_id, api_hash)

channels = [
    'ZemenExpress',
    'nevacomputer',
    'meneshayeofficial',
    'ethio_brand_collection',
    'Leyueqa'
]

async def fetch_messages(channel_username, limit=50):
    channel = await client.get_entity(channel_username)
    history = await client(GetHistoryRequest(
        peer=channel,
        limit=limit,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))

    messages = []
    for message in history.messages:
        if message.message:
            messages.append({
                "channel": channel_username,
                "date": str(message.date),
                "message": message.message
            })

    with open(f"data/raw/{channel_username}_messages.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)
    print(f"✅ Saved {len(messages)} messages from {channel_username}")

async def main():
    await client.start()
    for channel in channels:
        await fetch_messages(channel)

with client:
    client.loop.run_until_complete(main())
