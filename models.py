import sqlite3
from bcrypt import hashpw, gensalt, checkpw

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_user(phone, password):
    hashed_pw = hashpw(password.encode(), gensalt()).decode()
    db = get_db()
    db.execute("INSERT INTO users (phone, password) VALUES (?, ?)", (phone, hashed_pw))
    db.commit()
    db.close()

def check_user(phone, password):
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE phone = ?", (phone,)).fetchone()
    db.close()
    if user and checkpw(password.encode(), user["password"].encode()):
        return True
    return False

# Первичная настройка БД
def init_db():
    db = get_db()
    db.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )''')
    db.commit()
    db.close()
