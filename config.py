import os

class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "fallback-secret")

    DB_CONFIG = {
        "host": os.getenv("DB_HOST", "mysql.railway.internal"),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "yqsGfPBhkbFmFDiGzIdQoGQteYkAGktR"),
        "database": os.getenv("DB_NAME", "railway"),
        "port": int(os.getenv("DB_PORT", 3306))
    }
