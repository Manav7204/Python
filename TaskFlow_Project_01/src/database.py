import sqlite3
from src.exceptions import DatabaseError
from config import DATABASE_NAME
import logging

logger = logging.getLogger(__name__)


def create_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    return conn, cursor


def create_table():
    conn = None

    try:
        conn, cursor = create_connection()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT NOT NULL
            )
        """)

    except sqlite3.Error as e:
        raise DatabaseError("Failed to initialize the database.") from e

    finally:
        if conn:
            conn.commit()
            conn.close()
