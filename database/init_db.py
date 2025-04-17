import sqlite3
import os

# Get the absolute path of the current file (init_db.py)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Join that with the filename to form a full path
db_path = os.path.join(base_dir, "employee_attrition.db")

# Now connect and create table
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("manager", "1234"))
except sqlite3.IntegrityError:
    print("Manager already exists.")

conn.commit()
conn.close()
