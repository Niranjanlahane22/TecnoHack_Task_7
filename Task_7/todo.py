import json
from datetime import datetime

# Define the path to the JSON file for storing tasks
TASKS_FILE = 'tasks.json'

# Try to load existing tasks from the file
try:
    with open(TASKS_FILE, 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def save_tasks():
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description, priority, due_date):
    """Add a new task."""
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks()

def remove_task(task_id):
    """Remove a task by its ID."""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks()

def mark_task_completed(task_id):
    """Mark a task as completed."""
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
    save_tasks()

def list_tasks():
    """List all tasks."""
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")

def main():
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task Completed")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(description, priority, due_date)
        elif choice == "2":
            task_id = int(input("Enter task ID to remove: "))
            remove_task(task_id)
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
