import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
    HF_ACCESS_TOKEN = os.getenv("HF_ACCESS_TOKEN")
    HF_MODEL_NAME = os.getenv("HF_MODEL_NAME", "")
    MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "10"))

config = Config()
print(f"TELEGRAM_BOT_TOKEN: {repr(config.TG_BOT_TOKEN)}")
print(f"HF_ACCESS_TOKEN: {repr(config.HF_ACCESS_TOKEN)}")
print(f"HF_MODEL_NAME: {repr(config.HF_MODEL_NAME)}")
print(f"MAX_FILE_SIZE_MB: {config.MAX_FILE_SIZE_MB}")