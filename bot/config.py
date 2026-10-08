import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "8253156944:AAHH7XHhFgV6Rr3unpSGEt_8fEEzvDUxAig")
    TELEGRAM_API = int(os.getenv("TELEGRAM_API", "24955235"))
    TELEGRAM_HASH = os.getenv("TELEGRAM_HASH", "f317b3f7bbe390346d8b46868cff0de8")
    OWNER_ID = int(os.getenv("OWNER_ID", "5706788169"))
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Uploader:Uploader@cluster0.ba0ppxa.mongodb.net/?retryWrites=true&w=majority")
