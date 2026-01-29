from dotenv import load_dotenv
import os

load_dotenv()
class Settings:
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",0)


settings = Settings()
