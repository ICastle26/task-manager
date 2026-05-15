Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> tasks = []
... 
... def show_menu():
...     print("\n--- Task Manager ---")
...     print("1. Add a task")
...     print("2. View tasks")
...     print("3. Mark task as complete")
...     print("4. Delete a task")
...     print("5. Exit")
... 
... def add_task():
...     task = input("Enter a new task: ")
...     tasks.append({"task": task, "completed": False})
...     print("Task added!")
... 
... def view_tasks():
...     if not tasks:
...         print("No tasks yet.")
...         return
... 
...     print("\nYour Tasks:")
...     for i, t in enumerate(tasks, start=1):
...         status = "✔️" if t["completed"] else "❌"
...         print(f"{i}. {t['task']} [{status}]")
... 
... def complete_task():
...     view_tasks()
...     choice = int(input("Enter task number to mark complete: "))
...     tasks[choice - 1]["completed"] = True
...     print("Task marked as complete!")
... 
... def delete_task():
...     view_tasks()
...     choice = int(input("Enter task number to delete: "))
...     tasks.pop(choice - 1)
...     print("Task deleted!")
... 
while True:
    show_menu()
    option = input("Choose an option: ")

    if option == "1":
        add_task()
    elif option == "2":
        view_tasks()
    elif option == "3":
        complete_task()
    elif option == "4":
        delete_task()
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
