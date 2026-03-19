# Chat Plays

A customizable Twitch Plays program that lets your Twitch chat control games by translating chat messages into keyboard inputs.

## Requirements

- Python 3.10+
- A Twitch account
- A Twitch OAuth token

## Setup

### 1. Create a virtual environment (first time only)

```bash
python -m venv venv
```

### 2. Activate the virtual environment

```powershell
.\venv\Scripts\activate
```

You'll see `(venv)` appear at the start of your terminal line. This means you're inside the virtual environment.

### 3. Install dependencies (first time only)

```bash
pip install -r requirements.txt
```

### 4. Set up your Twitch credentials

1. Copy `.env.example` to a new file called `.env`
2. Go to [twitchtokengenerator.com](https://twitchtokengenerator.com)
3. Click **"Bot Chat Token"**
4. Authorize with your Twitch account
5. Copy the token (starts with `oauth:`) and paste it into `.env`
6. Fill in your channel name (lowercase)

Your `.env` should look like this:
```
TWITCH_TOKEN=oauth:abc123yourtokenhere
TWITCH_CHANNEL=yourchannelname
```

> **Important:** Never share your `.env` file or commit it to Git. The `.gitignore` is already set up to prevent this.

## Running

### Start the Twitch Listener

```powershell
.\venv\Scripts\activate
python twitch_listener.py
```

If everything is set up correctly, you'll see:
```
==================================================
  Bot is online!
  Logged in as : your_bot_name
  Listening to : your_channel
==================================================
```

Now type something in your Twitch chat — it should appear in the console as `[username]: message`.

Press `Ctrl+C` to stop the bot.

## Project Structure

```
chat-plays/
├── venv/                 # Python virtual environment (not committed)
├── .env                  # Your secret credentials (not committed)
├── .env.example          # Template showing what credentials are needed
├── .gitignore            # Keeps secrets and junk out of Git
├── requirements.txt      # Locked library versions
├── twitch_listener.py    # Connects to Twitch chat and reads messages
├── PLAN.md               # Architecture plan
├── TASKS.md              # Step-by-step progress tracker
└── README.md             # This file
```
