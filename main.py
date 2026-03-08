# check if tasks.json exists, if not create it
import argparse
from task_manager import TaskManager, TaskNotFoundError
from constants import VALID_STATUSES


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
    parser_list.add_argument(
        "status",
        nargs="?",
        choices=VALID_STATUSES,
        help="Filter tasks by status",
    )

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
    try:
        # Handle commands
        if args.command == "add":
            new_task = manager.add_task(" ".join(args.text))
            print(f"Added task with id {new_task['id']} : {new_task['description']}")
        elif args.command == "list":
            tasks = manager.list_tasks(args.status)
            print(f"Tasks ({args.status if args.status else 'all'}):")
            if not tasks:
                print("No tasks to show.")
            for task in tasks:
                print(
                    f"ID: {task['id']:2d}, Status: {task['status']:12} - {task['description']}"
                )
        elif args.command == "update":
            manager.update_task(args.id, " ".join(args.text))
            print(f"Task with ID {args.id} updated successfully.")
        elif args.command == "mark-in-progress":
            manager.mark_in_progress(args.id)
            print(f"Task with ID {args.id} marked as in-progress.")
        elif args.command == "mark-done":
            manager.mark_done(args.id)
            print(f"Task with ID {args.id} marked as done.")
        elif args.command == "delete":
            manager.delete_task(args.id)
            print(f"Task with ID {args.id} deleted successfully.")
        else:
            # This handles the case where no command is provided
            parser.print_help()
    except TaskNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
