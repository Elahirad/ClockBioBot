from pyrogram import Client

Bot = Client("my_account", api_id=input("Enter API ID :"), api_hash=input("Enter API HASH :"))
print(Bot.export_session_string())