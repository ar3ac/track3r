from storage import load_tasks, write_tasks
from datetime import datetime
from constants import DEFAULT_STATUS, VALID_STATUSES, STATUS_IN_PROGRESS, STATUS_DONE


class TaskNotFoundError(Exception):
    """Custom exception for when a task is not found."""
    pass

class TaskManager:
    def __init__(self):
        self.tasks_list = load_tasks()

    def now_iso(self):
        return datetime.now().isoformat() + "Z"  # Adding 'Z' to indicate UTC time

    def get_task(self, task_id):
        task = next((task for task in self.tasks_list if task["id"] == task_id), None)
        if task is None:
            raise TaskNotFoundError(f"No task found with ID: {task_id}")
        return task

    def add_task(self, description):
        if not description:
            raise ValueError("Task description cannot be empty.")
        if self.tasks_list:
            nuovo_id = max(task["id"] for task in self.tasks_list) + 1
        else:
            nuovo_id = 1
        new_task = {
            "id": nuovo_id,
            "description": description,
            "status": DEFAULT_STATUS,
            "created_at": self.now_iso(),
            "updated_at": self.now_iso(),
        }
        self.tasks_list.append(new_task)
        write_tasks(self.tasks_list)
        return new_task

    def list_tasks(self, status_filter=None):
        if status_filter and status_filter not in VALID_STATUSES:
            return []  # O potremmo sollevare un errore, ma per ora va bene così
        if status_filter:
            return [task for task in self.tasks_list if task["status"] == status_filter]
        return self.tasks_list

    def update_task(self, task_id, new_description):
        task = self.get_task(task_id)  # This will raise TaskNotFoundError if not found
        task["description"] = new_description
        task["updated_at"] = self.now_iso()
        write_tasks(self.tasks_list)
        return task

    def mark_in_progress(self, task_id):
        task = self.get_task(task_id)
        task["status"] = STATUS_IN_PROGRESS
        task["updated_at"] = self.now_iso()
        write_tasks(self.tasks_list)
        return task

    def mark_done(self, task_id):
        task = self.get_task(task_id)
        task["status"] = STATUS_DONE
        task["updated_at"] = self.now_iso()
        write_tasks(self.tasks_list)
        return task

    def delete_task(self, task_id):
        task_to_delete = self.get_task(task_id)
        self.tasks_list.remove(task_to_delete)
        write_tasks(self.tasks_list)
        # For delete, returning True on success is fine
        return True
