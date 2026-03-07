# check if tasks.json exists, if not create it
import argparse
from storage import load_tasks, write_tasks
from task_manager import TaskManager


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

    manager = TaskManager()
    # Handle commands
    # add: add a new task with the provided text
    if args.command == "add":
        # print("Add command selected. Task description:", " ".join(args.text))
        new_task = manager.add_task(" ".join(args.text))
        print(f"Added task with id {new_task['id']} : {new_task['description']}")
    elif args.command == "list":
        tasks = manager.list_tasks(args.filter)
        print(f"Tasks ({args.filter if args.filter else 'all'}):")
        for task in tasks:
            print(
                f"ID: {task['id']:2d}, Status: {task['status']:12} - {task['description']}"
            )
    elif args.command == "update":
        task_updated = manager.update_task(args.id, " ".join(args.text))
        if task_updated:
            print(f"Task with ID {args.id} updated successfully.")
        else:
            print(f"No task found with ID: {args.id}")
    elif args.command == "mark-in-progress":
        task_updated = manager.mark_in_progress(args.id)
        if task_updated:
            print(f"Task with ID {args.id} marked as in-progress.")
        else:
            print(f"No task found with ID: {args.id}")
    elif args.command == "mark-done":
        task_updated = manager.mark_done(args.id)
        if task_updated:
            print(f"Task with ID {args.id} marked as done.")
        else:
            print(f"No task found with ID: {args.id}")
    elif args.command == "delete":
        task_deleted = manager.delete_task(args.id)
        if task_deleted:
            print(f"Task with ID {args.id} deleted successfully.")
        else:
            print(f"No task found with ID: {args.id}")
    else:
        print(parser.print_help())


if __name__ == "__main__":
    main()
