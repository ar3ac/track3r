from rich.console import Console
from rich.table import Table


def display_tasks_table(tasks):
    """Displays a list of tasks in a formatted table using rich."""
    console = Console()

    if not tasks:
        console.print("[yellow]No tasks to show.[/yellow]")
        return

    table = Table(show_header=True, header_style="bold magenta", title="Tasks")
    table.add_column("ID", style="dim", width=4, justify="right")
    table.add_column("Status", width=12)
    table.add_column("Description", no_wrap=False)
    table.add_column("Created", style="dim", width=16)
    table.add_column("Updated", style="dim", width=16)

    status_colors = {
        "todo": "red",
        "in-progress": "yellow",
        "done": "green",
    }

    for task in tasks:
        status = task["status"]
        color = status_colors.get(status, "white")
        # Format ISO string to YYYY-MM-DD HH:MM
        created = task.get("created_at", "")[:16].replace("T", " ")
        updated = task.get("updated_at", "")[:16].replace("T", " ")
        table.add_row(
            str(task["id"]),
            f"[{color}]{status}[/{color}]",
            task["description"],
            created,
            updated,
        )

    console.print(table)


def display_success(message):
    console = Console()
    console.print(f"[bold green]Success:[/bold green] {message}")


def display_error(message):
    console = Console()
    console.print(f"[bold red]Error:[/bold red] {message}")
