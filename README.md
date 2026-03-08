# track3r - A Modern CLI Task Manager

`track3r` is a simple yet powerful command-line tool to manage your daily tasks. It features a clean, colorful, and modern interface, making task management from the terminal a pleasant experience.

### Demo

```
$ python main.py list
                                     Tasks
┏━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃   ID ┃ Status       ┃ Description                  ┃ Created          ┃ Updated          ┃
┡━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│    1 │ in-progress  │ Implement the core logic     │ 2023-10-27 10:00 │ 2023-10-27 11:30 │
│    5 │ done         │ Design the database schema   │ 2023-10-26 15:00 │ 2023-10-26 18:00 │
│   11 │ todo         │ Write the documentation      │ 2023-10-27 12:00 │ 2023-10-27 12:00 │
└──────┴──────────────┴──────────────────────────────┴──────────────────┴──────────────────┘
```

## ✨ Features

- **Colorful & Modern UI**: Uses `rich` to display tasks in a clean, readable table.
- **Status Tracking**: Manage tasks with `todo`, `in-progress`, and `done` statuses, each with its own color.
- **Persistent Storage**: All tasks are saved locally in a `tasks.json` file.
- **Simple Command Structure**: Intuitive commands for adding, listing, updating, and deleting tasks.
- **Robust Error Handling**: Clear error messages and proper exit codes for scripting and automation.

## 📋 Requirements

- Python 3.6+
- `rich` library

## 🚀 Installation

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/ar3ac/track3r.git
    cd track3r
    ```

2.  **Install dependencies:**
    ```sh
    pip install rich
    ```

## 💻 Usage

All commands are run from the project's root directory.

### Add a new task

A new task is always created with the `todo` status.

```sh
python main.py add "My new important task"
```

### List tasks

You can list all tasks or filter them by status.

```sh
# List all tasks
python main.py list

# List only tasks that are 'done'
python main.py list done
```

### Update a task's description

```sh
python main.py update <ID> "This is the new description"
```

### Change a task's status

```sh
# Mark a task as in-progress
python main.py mark-in-progress <ID>

# Mark a task as done
python main.py mark-done <ID>
```

### Delete a task

```sh
python main.py delete <ID>
```

## 🗺️ Roadmap

Here are some ideas for future improvements:

- **Search**: Implement a `search <keyword>` command to find tasks by text.
- **Sorting**: Add options to sort the task list (e.g., by update date, by status).
- **Unit Tests**: Increase code reliability by adding a test suite with `pytest`.
- **Export**: Add functionality to export tasks to other formats like CSV.
