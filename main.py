# check if tasks.json exists, if not create it
import json
import os


def check_tasks_file():
    if not os.path.exists("tasks.json"):
        with open("tasks.json", "w") as f:
            json.dump([], f)
            f.close()


def load_tasks():
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
        f.close()
    return tasks


def write_tasks(tasks):
    try:
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
            f.close()
    except Exception as e:
        print(f"Error writing tasks to file: {e}")


def main():
    check_tasks_file()
    print("Welcome to the task3r:")
    tasks_list = load_tasks()
    print(len(tasks_list))
    print(tasks_list)
    write_tasks(tasks_list)


if __name__ == "__main__":
    main()
