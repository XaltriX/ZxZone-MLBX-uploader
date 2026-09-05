import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5331375208:AAGw2IB5kXZ7U8x-AScLdMiBjbM0RcwXJAQ")
    TELEGRAM_API = int(os.getenv("TELEGRAM_API", "6534707"))
    TELEGRAM_HASH = os.getenv("TELEGRAM_HASH", "4bcc61d959a9f403b2f20149cbbe627a")
    OWNER_ID = int(os.getenv("OWNER_ID", "1430593323"))
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Uploader:Uploader@cluster0.ba0ppxa.mongodb.net/?retryWrites=true&w=majority")
