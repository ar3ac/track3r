import json
import os


def check_tasks_file():
    if not os.path.exists("tasks.json"):
        with open("tasks.json", "w") as f:
            json.dump([], f)
            f.close()


def load_tasks():
    check_tasks_file()
    try:
        with open("tasks.json", "r") as f:
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise ValueError("The tasks.json file is corrupted and cannot be read.")


def write_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
