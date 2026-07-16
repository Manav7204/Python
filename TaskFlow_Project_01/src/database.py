import sqlite3

DATABASE_NAME = 'data/task.db'
def create_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    return conn, cursor

def create_table():
    conn, cursor = create_connection()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def insert_task():
    conn, cursor = create_connection()

    task_title = input("Enter the Title of the task.\n>").strip()

    if task_title:
        cursor.execute(
        "Insert INTO tasks (title) VALUES (?)",
        (task_title,)               
        )
        conn.commit()
        conn.close()
        print("Task added Successfully\n")
    else:
        conn.close()
        print("\nTask cannot be empty!\n")
        return None