import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN = int(os.getenv('ADMIN'))
POSTGRES_URI = os.getenv('POSTGRES_URI')
CHANNEL = os.getenv('CHANNEL')
JOINCHAT_URL = os.getenv('JOINCHAT_URL')
