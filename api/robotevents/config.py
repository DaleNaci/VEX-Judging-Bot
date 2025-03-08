import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ROBOTEVENTS_TOKEN")
BASE_URL = "https://www.robotevents.com/api/v2"