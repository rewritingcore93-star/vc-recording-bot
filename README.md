# vc-recording-bot

# Telegram VC Recording Bot

A bot that automatically records voice chats in Telegram groups to ensure member safety.

## Features
- 🎙️ Automatically joins voice chats
- 🔴 Records when members speak
- ⏱️ 15-minute file segments
- 📤 Sends recordings to owner's DM
- 🔄 Auto-reconnects on network issues
- 📊 Web monitoring dashboard

## Setup
1. Clone this repository
2. Copy `.env.example` to `.env` and fill in your credentials
3. Run `./start.sh`

## Commands
- `/start` - Get bot info
- `/status` - Check bot status (owner only)
- `/stats` - View statistics (owner only)

## Requirements
- Python 3.8+
- FFmpeg
- Telegram Bot Token
- Telegram API ID & Hash
