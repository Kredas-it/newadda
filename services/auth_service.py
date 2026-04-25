from database.db import get_db
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(name, password):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    UserName VARCHAR(100),
    Password VARCHAR(255))""")

    conn.commit()
    hashed_password = generate_password_hash(password)

    cur.execute(
        "INSERT INTO Users(UserName, Password) VALUES (%s, %s)",
        (name, hashed_password)
    )
    conn.commit()

    return {"message": "User registered successfully"}


def login_user(name, password):
    conn = get_db()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM Users WHERE UserName=%s", (name,))
    user = cur.fetchone()

    if not user:
        return {"error": "User not found"}, 404

    if not check_password_hash(user['Password'], password):
        return {"error": "Invalid password"}, 401

    return user


def get_user_profile(username):
    conn = get_db()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT UserName FROM Users WHERE UserName=%s", (username,))
    return cur.fetchone()
