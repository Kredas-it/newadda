import mysql.connector
from config import Config

def get_db():
    return mysql.connector.connect(**Config.DB_CONFIG)
