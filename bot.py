from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import UserAlreadyParticipantError

api_id = 1234
api_hash = ""

CHANNELS = [
    {
        "channel_username": "",
        "channel_id": -10012345,
        "chat_username": "",
        "chat_id": -10012345,
    },
]

TRIGGER_TEXTS = ["первый"]
MESSAGE_TEXT = "а"

client = TelegramClient(
    "session/my_account",
    api_id,
    api_hash,
    device_model='test',
    system_version='1.0.0',
    app_version='test app'
)

@client.on(events.NewMessage(chats=[p["chat_id"] for p in CHANNELS]))
async def handler(event):
    if event.fwd_from and event.fwd_from.from_id and getattr(event.fwd_from.from_id, "channel_id", None):
        channel_id = f'-100{event.fwd_from.from_id.channel_id}'

        for pair in CHANNELS:
            if event.chat_id == pair["chat_id"] and channel_id == pair["channel_id"]:
                text = event.raw_text.lower()

                if any(trigger in text for trigger in TRIGGER_TEXTS):
                    await event.reply(MESSAGE_TEXT)
                    print(f"Replied in {pair['chat_username']} to trigger '{text}'")
                break

async def main():
    for pair in CHANNELS:
        for username in [pair["channel_username"], pair["chat_username"]]:
            try:
                await client(JoinChannelRequest(username))
                print(f"Joined {username}")
            except UserAlreadyParticipantError:
                print(f"Already a member of {username}")
            except Exception as e:
                print(f"Failed to join {username}: {e}")

    print("Bot is running")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
