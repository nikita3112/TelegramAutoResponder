# Telegram Auto-Responder Bot (Telethon + Docker)

This project is a **Telegram auto-responder bot** built with [Telethon](https://github.com/LonamiWebs/Telethon).  
It listens to specified chats and automatically replies when trigger words are detected.  
The bot runs inside a **Docker container** using `docker-compose`.

---

## ✨ Features

- Automatically joins configured **channels** and **chats**.
- Listens for **forwarded messages** from a specific channel.
- Replies when a trigger word is found.
- Logs all actions.

---

## ⚙️ Requirements

- Docker
- Docker Compose

---

## 🚀 Setup

### 1. Clone repository

```bash
git clone https://github.com/yourname/telegram-autoresponder.git
cd telegram-autoresponder
```

### 2. Configure environment

Use your Telegram API credentials:

```python
API_ID=123456
API_HASH=your_api_hash_here
```

### 3. Configure channels

Edit the `CHANNELS` list in `bot.py`:

```python
CHANNELS = [
    {
        "channel_username": "channel_username",
        "channel_id": -100XXXXX,
        "chat_username": "chat_username",
        "chat_id": -100XXXXX,
    },
]
```

### 4. Build and run the bot

```bash
docker-compose up --build -d
```

---

## 🛑 Stopping the bot

```bash
docker-compose down
```

---

## 📜 Logs

To see logs in real time:

```bash
docker-compose logs -f
```

---

## ⚠️ Disclaimer

This bot is for **educational purposes only**.  
Use responsibly and make sure you comply with [Telegram Terms of Service](https://core.telegram.org/terms).
