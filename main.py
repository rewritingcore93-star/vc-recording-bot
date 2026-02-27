#!/usr/bin/env python3
"""
VC Recording Bot - Main Entry Point
"""
import asyncio
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import Config
from src.utils.logger import setup_logger
from src.handlers.notifications import notify_owner
from src.utils.monitoring import start_monitoring
from src.recorder import RecordingManager
import pyrogram
from pytgcalls import PyTgCalls

logger = setup_logger()

class VCRecorderBot:
    def __init__(self):
        self.config = Config()
        self.recording_manager = RecordingManager()
        
    async def start(self):
        """Start the bot"""
        logger.info("Starting VC Recording Bot...")
        
        # Initialize clients
        self.pyro_client = pyrogram.Client(
            "vc_recorder",
            api_id=self.config.API_ID,
            api_hash=self.config.API_HASH,
            bot_token=self.config.BOT_TOKEN
        )
        
        self.pytgcalls = PyTgCalls(self.pyro_client)
        
        # Start clients
        await self.pyro_client.start()
        await self.pytgcalls.start()
        
        # Notify owner
        await notify_owner(
            self.pyro_client,
            "🚀 Bot started successfully!\nMonitoring voice chats...",
            "success"
        )
        
        # Start monitoring
        asyncio.create_task(start_monitoring(self))
        
        logger.info("Bot is running!")
        
        # Keep running
        await self.pyro_client.idle()

async def main():
    bot = VCRecorderBot()
    await bot.start()

if __name__ == "__main__":
    asyncio.run(main())
