import sqlite3
import logging

logger = logging.getLogger(__name__)

DATABASE_NAME = 'data/task.db'
def create_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    return conn, cursor

def create_table():
    try:
        conn, cursor = create_connection()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
            )
        """)

    except sqlite3.Error as error:
        logger.error(f"Database error: {error}")
    
    finally:
        if conn:
            conn.commit()
            conn.close()

def insert_task(task_title):
    conn, cursor = create_connection()
    
    cursor.execute(
    "Insert INTO tasks (title) VALUES (?)",
    (task_title,)              
    )

    inserted_id = cursor.lastrowid

    conn.commit()
    conn.close()
    return inserted_id

def read_tasks():
    conn, cursor = create_connection()

    cursor.execute(
        """SELECT * FROM tasks;"""
    )
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def get_task_by_id(task_id):
    conn, cursor = create_connection()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    task = cursor.fetchone()

    conn.close()

    return task

def alter_task(task_title, task_id):
    conn, cursor = create_connection()

    cursor.execute(
        """UPDATE tasks
        SET title = ?
        WHERE id = ?""",
        (task_title, task_id)
    )
    
    conn.commit()
    conn.close()


def retrieve_tasks(keyword):
    conn, cursor = create_connection()

    cursor.execute(
        """SELECT * FROM tasks
        WHERE title LIKE ?""",
        (f"%{keyword}%",)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks

def delete_task_record(task_id):
    conn, cursor = create_connection()

    cursor.execute(
        """DELETE FROM tasks
        WHERE id = ?""",
        (task_id,)
    )
    
    conn.commit()
    conn.close()