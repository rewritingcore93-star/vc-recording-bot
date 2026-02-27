import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    API_ID = int(os.getenv('API_ID', 0))
    API_HASH = os.getenv('API_HASH')
    OWNER_ID = int(os.getenv('OWNER_ID', 0))
    
    # Recording settings
    MAX_RECORDING_DURATION = int(os.getenv('MAX_RECORDING_DURATION', 900))
    SILENT_TIMEOUT = int(os.getenv('SILENT_TIMEOUT', 30))
    
    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RECORDINGS_DIR = os.path.join(BASE_DIR, 'recordings')
    LOGS_DIR = os.path.join(BASE_DIR, 'logs')
    
    # Web dashboard
    WEB_DASHBOARD_PORT = int(os.getenv('WEB_DASHBOARD_PORT', 5000))
    
    # Ensure directories exist
    os.makedirs(RECORDINGS_DIR, exist_ok=True)
    os.makedirs(LOGS_DIR, exist_ok=True)
