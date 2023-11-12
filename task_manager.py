import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# Create table to store tasks
c.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    task_name TEXT NOT NULL,
    status TEXT CHECK( status IN ('open','complete') ) NOT NULL DEFAULT 'open',
    priority INTEGER CHECK( priority IN (1,2,3) ) NOT NULL
)
''')
conn.commit()

def show_open_tasks():
    c.execute("SELECT * FROM tasks WHERE status='open'")
    for row in c.fetchall():
        print(row)

def show_completed_tasks():
    c.execute("SELECT * FROM tasks WHERE status='complete'")
    for row in c.fetchall():
        print(row)

def show_all_tasks():
    c.execute("SELECT * FROM tasks")
    for row in c.fetchall():
        print(row)

def add_task(task_name, priority):
    c.execute("INSERT INTO tasks (task_name, status, priority) VALUES (?, 'open', ?)", (task_name, priority))
    conn.commit()

def mark_task_as_complete(task_id):
    c.execute("UPDATE tasks SET status='complete' WHERE id=?", (task_id,))
    conn.commit()

def delete_task(task_id):
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

# Function to display menu and get user choice
def menu():
    while True:
        print("""
        1. Show Open Tasks
        2. Show Completed Tasks
        3. Show All Tasks
        4. Add Task
        5. Mark Task as Complete
        6. Delete Task
        7. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            show_open_tasks()
        elif choice == "2":
            show_completed_tasks()
        elif choice == "3":
            show_all_tasks()
        elif choice == "4":
            task_name = input("Enter task name: ")
            priority = int(input("Enter priority (1, 2, 3): "))
            add_task(task_name, priority)
        elif choice == "5":
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_task_as_complete(task_id)
        elif choice == "6":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "7":
            break
        else:
            print("Invalid choice, please try again.")

menu()  # Call the menu function to start the program

# Close the connection to the database
conn.close()
