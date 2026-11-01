"""
Task Manager - a simple command-line to-do app.

Tasks are saved to tasks.json so they're still there the next time you run it.
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks():
    """Load saved tasks from disk, or start with an empty list."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Couldn't read saved tasks, starting fresh.")
        return []


def save_tasks(tasks):
    """Write the current task list to disk."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return False

    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "[x]" if t["completed"] else "[ ]"
        print(f"{i}. {status} {t['task']}")
    return True


def pick_task(tasks, prompt):
    """Ask for a task number and return its index, or None if the input is invalid."""
    choice = input(prompt).strip()
    if not choice.isdigit() or not 1 <= int(choice) <= len(tasks):
        print(f"Please enter a number between 1 and {len(tasks)}.")
        return None
    return int(choice) - 1


def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if not task:
        print("Task can't be empty.")
        return
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added!")


def complete_task(tasks):
    if not view_tasks(tasks):
        return
    index = pick_task(tasks, "Enter task number to mark complete: ")
    if index is not None:
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete!")


def delete_task(tasks):
    if not view_tasks(tasks):
        return
    index = pick_task(tasks, "Enter task number to delete: ")
    if index is not None:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")


def main():
    tasks = load_tasks()
    actions = {
        "1": add_task,
        "2": view_tasks,
        "3": complete_task,
        "4": delete_task,
    }

    while True:
        show_menu()
        option = input("Choose an option: ").strip()

        if option == "5":
            print("Goodbye!")
            break
        elif option in actions:
            actions[option](tasks)
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
