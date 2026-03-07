# check if tasks.json exists, if not create it
import json
import os
import argparse
from datetime import datetime


def now_iso():
    return datetime.now().isoformat() + "Z"  # Adding 'Z' to indicate UTC time


def check_tasks_file():
    if not os.path.exists("tasks.json"):
        with open("tasks.json", "w") as f:
            json.dump([], f)
            f.close()


def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            f.close()
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
            json.dump(tasks, f)
            f.close()
    except Exception as e:
        print(f"Error writing tasks to file: {e}")


def main():
    parser = argparse.ArgumentParser(description='"track3r: a cli task manager"')

    # commands
    subparsers = parser.add_subparsers(dest="command", help="Commands to manage tasks")

    # ADD
    parser_add = subparsers.add_parser("add", help="add a new task")
    parser_add.add_argument(
        "text", help="task description", nargs="+"
    )  # task description as a required argument

    # LIST
    parser_list = subparsers.add_parser(
        "list", help="Show tasks ( with optional filters : todo, in-progress, done )"
    )
    list_subparsers = parser_list.add_subparsers(dest="filter", help="Filter to apply")

    # list subcommands
    list_subparsers.add_parser("todo", help="Show only todos to do")
    list_subparsers.add_parser("in-progress", help="Show only todos in progress")
    list_subparsers.add_parser("done", help="Show only completed todos")

    # UPDATE
    parser_update = subparsers.add_parser("update", help="update a task")
    parser_update.add_argument("id", type=int, help="ID of the task to update")

    # DELETE
    parser_delete = subparsers.add_parser("delete", help="delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    # MARK IN PROGRESS
    parser_mark_in_progress = subparsers.add_parser(
        "mark-in-progress", help="mark a task as in progress"
    )
    parser_mark_in_progress.add_argument("id", type=int, help="ID of the task to mark")

    # MARK DONE
    parser_mark_done = subparsers.add_parser("mark-done", help="mark a task as done")
    parser_mark_done.add_argument("id", type=int, help="ID of the task to mark")

    args = parser.parse_args()

    tasks_list = load_tasks()
    # Handle commands
    # add: add a new task with the provided text
    if args.command == "add":
        if not args.text:
            print("Error: 'add' command requires a task description.")
            return
        # id dynamic,find the maximum id in the current tasks list and add 1 to it for the new task
        if tasks_list:
            nuovo_id = max(task["id"] for task in tasks_list) + 1
        else:
            nuovo_id = 1

        new_task = {
            "id": nuovo_id,
            "description": args.text,
            "status": "todo",
            "created_at": now_iso(),  # This should be the current timestamp
            "updated_at": now_iso(),  # This should be the current timestamp
        }
        tasks_list = load_tasks()
        tasks_list.append(new_task)
        write_tasks(tasks_list)
    elif args.command == "update":
        pass
    elif args.command == "delete":
        pass
    elif args.command == "mark-in-progress":
        pass
    elif args.command == "mark-done":
        pass
    elif args.command == "list" and not hasattr(args, "filtro"):
        parser_list.print_help()
    elif args.command == "list":
        pass
    else:
        print(parser.print_help())

    check_tasks_file()
    print("Welcome to the task3r:")

    print(len(tasks_list))
    print(tasks_list)
    print(now_iso())
    write_tasks(tasks_list)


if __name__ == "__main__":
    main()
