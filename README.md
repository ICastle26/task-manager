# Task Manager (Python)

A command-line to-do app built in Python. Add tasks, check them off, and delete them. Your tasks are saved to a file, so they're still there the next time you open the app.

## Features
- Add, view, complete, and delete tasks
- Tasks are saved automatically to `tasks.json`
- Input validation, so a typo or an out-of-range number won't crash the program

## Tech Used
- Python 3 (standard library only, nothing to install)
- JSON for saving data

## How to Run
1. Install [Python 3](https://www.python.org/downloads/) if you don't have it.
2. Download or clone this repo:
   ```
   git clone https://github.com/ICastle26/task-manager.git
   cd task-manager
   ```
3. Run the app:
   ```
   python task_manager.py
   ```

## Example
```
--- Task Manager ---
1. Add a task
2. View tasks
3. Mark task as complete
4. Delete a task
5. Exit
Choose an option: 2

Your Tasks:
1. [x] Finish networking discussion post
2. [ ] Update portfolio website
```

## What I Learned
- Organizing a program into small, reusable functions
- Reading and writing files with JSON
- Validating user input and handling errors gracefully
