# util.py

from dotenv import load_dotenv, get_key
import os



dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')
