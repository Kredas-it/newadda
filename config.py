import os

class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "fallback-secret")

    DB_CONFIG = {
        "host": os.getenv("mysql.railway.internal"),
        "user": os.getenv("root"),
        "password": os.getenv("yqsGfPBhkbFmFDiGzIdQoGQteYkAGktR"),
        "database": os.getenv("railway"),
        "port": int(os.getenv("DB_PORT", 3306))
    }
