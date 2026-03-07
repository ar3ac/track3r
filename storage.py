import json
import os


def check_tasks_file():
    if not os.path.exists("tasks.json"):
        with open("tasks.json", "w") as f:
            json.dump([], f)
            f.close()


def load_tasks():
    check_tasks_file()
    tasks = []
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print("File non trovato!")
    except json.JSONDecodeError:
        print("File JSON corrotto o malformato!")
    except Exception as e:
        print(f"Errore generico: {e}")
    return tasks


def write_tasks(tasks):
    try:
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)
            f.close()
    except Exception as e:
        print(f"Error writing tasks to file: {e}")
