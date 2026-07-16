import sqlite3

DATABASE_NAME = 'data/task.db'
def create_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    return conn, cursor

def create_table():
    conn ,cursor = create_connection()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
