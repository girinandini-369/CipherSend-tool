# db_utils.py
import sqlite3
from hashlib import sha256
from datetime import datetime

DB = "files.db"

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS files(
        id INTEGER PRIMARY KEY,
        filename TEXT,
        enc_filename TEXT,
        timestamp TEXT,
        key_hash TEXT
    )
    """)
    conn.commit()
    conn.close()

def log_file(fn, enc_fn, pw):
    conn = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO files(filename,enc_filename,timestamp,key_hash) VALUES (?,?,?,?)",
        (fn, enc_fn, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), sha256(pw.encode()).hexdigest())
    )
    conn.commit()
    conn.close()