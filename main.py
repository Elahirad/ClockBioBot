from pyrogram import Client
from pyrogram.errors import FloodWait
import datetime
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
# Getting API ID and API HASH
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bio_string = os.environ.get("BIO_STR")
session_name = os.environ.get("SESSION_NAME")
print(api_id)
print(api_hash)
print(bio_string)
print(session_name)


async def main():
    async with Client(api_id=api_id, api_hash=api_hash, session_name=session_name) as BioBotClient:
        try:
            while True:
                now = datetime.datetime.now()
                if (now.second == 0):
                    string = bio_string + now.strftime("%H:%M")
                    await BioBotClient.update_profile(bio=string)
                    print("Bio Updated with : " + string)
                    await asyncio.sleep(10)
                await asyncio.sleep(0.5)
                print(now.second)
        except FloodWait as e:
            await asyncio.sleep(e.x)

print("Program working !!!")
asyncio.run(main())
