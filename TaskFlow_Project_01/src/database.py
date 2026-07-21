import sqlite3
from src.models.task import Task
from src.models.status import Status
import logging

logger = logging.getLogger(__name__)

DATABASE_NAME = "data/task.db"


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
            title TEXT NOT NULL,
            status TEXT NOT NULL
            )
        """)

    except sqlite3.Error as error:
        logger.error(f"Database error: {error}")

    finally:
        if conn:
            conn.commit()
            conn.close()


def insert_task(task):
    conn, cursor = create_connection()

    cursor.execute(
        """Insert INTO tasks (title, status) VALUES (?, ?)""",
        (task.title, task.status.name),
    )

    inserted_id = cursor.lastrowid

    conn.commit()
    conn.close()
    return inserted_id


def read_tasks():
    conn, cursor = create_connection()

    cursor.execute("""SELECT * FROM tasks;""")
    rows = cursor.fetchall()

    tasks = []

    for row in rows:
        tasks.append(Task(row[0], row[1], Status(row[2])))

    conn.close()
    return tasks


def get_task_by_id(task_id):
    conn, cursor = create_connection()

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))

    row = cursor.fetchone()

    if row is None:
        conn.close()
        return None

    task = Task(row[0], row[1], Status(row[2]))

    conn.close()

    return task


def alter_task(task):
    conn, cursor = create_connection()

    cursor.execute(
        """UPDATE tasks
        SET title = ?, status = ?
        WHERE id = ?""",
        (task.title, task.status.name, task.id),
    )

    conn.commit()
    conn.close()


def retrieve_tasks(keyword):
    conn, cursor = create_connection()

    cursor.execute(
        """SELECT * FROM tasks
        WHERE title LIKE ?""",
        (f"%{keyword}%",),
    )

    rows = cursor.fetchall()

    tasks = []

    for row in rows:
        task = Task(row[0], row[1], Status(row[2]))
        tasks.append(task)

    conn.close()
    return tasks


def delete_task_record(task):
    conn, cursor = create_connection()

    cursor.execute(
        """DELETE FROM tasks
        WHERE id = ?""",
        (task.id,),
    )

    conn.commit()
    conn.close()
