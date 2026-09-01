import sqlite3


DB_NAME = "tasks.db"


def initialize_database():
    """Create the tasks table if it does not exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            due_date TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def add_task(title, due_date):
    """Add a new task to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, completed, due_date) VALUES (?, 0, ?)",
        (title, due_date),
    )
    conn.commit()
    conn.close()


def list_tasks():
    """Return all tasks from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    rows = cursor.execute(
        "SELECT id, title, completed, due_date FROM tasks ORDER BY id"
    ).fetchall()
    conn.close()
    return rows


def mark_task_complete(task_id):
    """Mark a task as complete."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (task_id,),
    )
    conn.commit()
    conn.close()


def delete_task(task_id):
    """Delete a task from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_database()
    print("To-Do Tracker ready!")
    print("Current tasks:")
    for task in list_tasks():
        print(task)
