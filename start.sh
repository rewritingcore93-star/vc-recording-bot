#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}🎙️ Starting VC Recording Bot${NC}"

# Check if .env exists
if [ ! -f .env ]; then
    echo -e "${RED}❌ .env file not found!${NC}"
    echo -e "${YELLOW}Please create .env file with your credentials${NC}"
    exit 1
fi

# Create necessary directories
mkdir -p recordings logs

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✓ Python version: $python_version${NC}"

# Install/update requirements
echo -e "${YELLOW}📦 Installing requirements...${NC}"
pip install -r requirements.txt

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo -e "${RED}❌ ffmpeg not found!${NC}"
    echo -e "${YELLOW}Please install ffmpeg:${NC}"
    echo "  Ubuntu: sudo apt install ffmpeg"
    echo "  Mac: brew install ffmpeg"
    exit 1
fi
echo -e "${GREEN}✓ ffmpeg found${NC}"

# Start the bot
echo -e "${GREEN}🚀 Bot is starting...${NC}"
echo -e "${YELLOW}Check logs/vc_bot.log for details${NC}"
echo -e "${GREEN}──────────────────────────────${NC}"

python3 -m src.main
