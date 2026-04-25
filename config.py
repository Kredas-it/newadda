import os

class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "fallback-secret")

    DB_CONFIG = {
        "host": os.getenv("DB_HOST", "localhost"),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", ""),
        "database": os.getenv("DB_NAME", "mydb"),
        "port": int(os.getenv("DB_PORT", 3306))
    }
