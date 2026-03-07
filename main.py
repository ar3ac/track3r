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
    check_tasks_file()
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
            json.dump(tasks, f, indent=4)
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
    parser_update.add_argument(
        "text", help="new task description", nargs="+"
    )  # new task description as a required argument

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
            # add description by joining the list of words in args.text with spaces
            "description": args.text[0] if len(args.text) == 1 else " ".join(args.text),
            "status": "todo",
            "created_at": now_iso(),  # This should be the current timestamp
            "updated_at": now_iso(),  # This should be the current timestamp
        }
        tasks_list = load_tasks()
        tasks_list.append(new_task)
        write_tasks(tasks_list)
        # show the new task added with its id and description and the updated task list
        print(f"Task added successfully with ID: {nuovo_id}")
        print("Updated task list:")
        for task in tasks_list:
            print(
                f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}"
            )
    elif args.command == "update":
        print("Update command selected. Task ID to update:", args.id)
        # find the task with the provided id and update its description with the new text
        task_to_update = next(
            (task for task in tasks_list if task["id"] == args.id), None
        )
        if task_to_update:
            task_to_update["description"] = " ".join(args.text)
            task_to_update["updated_at"] = now_iso()
            write_tasks(tasks_list)
            print(f"Task with ID {args.id} updated successfully.")
        else:
            print(f"No task found with ID: {args.id}")
    elif args.command == "delete":
        print("Delete command selected. Task ID to delete:", args.id)
    elif args.command == "mark-in-progress":
        print("Mark in-progress command selected. Task ID to mark:", args.id)
        task_to_update = next(
            (task for task in tasks_list if task["id"] == args.id), None
        )
        if task_to_update:
            task_to_update["status"] = "in-progress"
            task_to_update["updated_at"] = now_iso()
            write_tasks(tasks_list)
            print(f"Task with ID {args.id} marked as in-progress.")
        else:
            print(f"No task found with ID: {args.id}")
    elif args.command == "mark-done":
        print("Mark done command selected. Task ID to mark:", args.id)
        task_to_update = next(
            (task for task in tasks_list if task["id"] == args.id), None
        )
        if task_to_update:
            task_to_update["status"] = "done"
            task_to_update["updated_at"] = now_iso()
            write_tasks(tasks_list)
            print(f"Task with ID {args.id} marked as done.")
        else:
            print(f"No task found with ID: {args.id}")
    # se il comando è list e non ha un filtro, mostra tutte le attività senza filtri e ben formattate
    elif args.command == "list" and not args.filter:
        # list all tasks without filters and well formatted
        print("All tasks:")
        if len(tasks_list) == 0:
            print("No tasks found.")
            return
        for task in tasks_list:
            print(
                f"ID: {task['id']:2d}, status: {task['status']:10} - updated at: {task['updated_at']} - Description: {task['description']}"
            )
    elif args.command == "list" and args.filter == "todo":
        # list only todo tasks
        print("Todo tasks:")
        if len(tasks_list) == 0:
            print("No todo tasks found.")
            return
        for task in tasks_list:
            if task["status"] == "todo":
                print(
                    f"ID: {task['id']:2d}, status: {task['status']:12} - Description: {task['description']}"
                )
    elif args.command == "list" and args.filter == "in-progress":
        # list only in-progress tasks
        print("In-progress tasks:")
        if len(tasks_list) == 0:
            print("No in-progress tasks found.")
            return
        for task in tasks_list:
            if task["status"] == "in-progress":
                print(
                    f"ID: {task['id']:2d}, status: {task['status']:10} - Description: {task['description']}"
                )
    elif args.command == "list" and args.filter == "done":
        # list only done tasks
        print("Done tasks:")
        if len(tasks_list) == 0:
            print("No done tasks found.")
            return
        for task in tasks_list:
            if task["status"] == "done":
                print(
                    f"ID: {task['id']:2d}, status: {task['status']:10} - Description: {task['description']}"
                )
    else:
        print(parser.print_help())

    # print("Welcome to the task3r:")

    # print(len(tasks_list))
    # print(tasks_list)
    # print(now_iso())
    # write_tasks(tasks_list)


if __name__ == "__main__":
    main()
