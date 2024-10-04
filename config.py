from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
OSTROVOK_API_KEY = os.getenv("OSTROVOK_API_KEY")
