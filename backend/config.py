import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(__file__)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'traveloop_secret_key_change_me')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt_traveloop_secret_key_change_me')
    # Use MySQL if DATABASE_URL set, otherwise fallback to SQLite for easy local dev
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f"sqlite:///{os.path.join(BASE_DIR, 'traveloop.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
