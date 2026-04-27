import os

class Config:
    # JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "fallback-secret")

    DB_CONFIG = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME"),
        "port": int(os.getenv("DB_PORT"))
    }
