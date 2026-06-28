import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


class Config:
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    PORT = int(os.getenv("PORT", 5000))
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "phishing_detector")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "change_this_secret")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES_MINUTES", 1440))
    )
    VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY", "")
    RATE_LIMIT = os.getenv("RATE_LIMIT", "100 per hour")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@example.com")
