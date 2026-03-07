from storage import load_tasks, write_tasks
from datetime import datetime


class TaskManager:
    def __init__(self):
        self.tasks_list = load_tasks()

    def now_iso(self):
        return datetime.now().isoformat() + "Z"  # Adding 'Z' to indicate UTC time

    def get_task(self, task_id):
        return next((task for task in self.tasks_list if task["id"] == task_id), None)

    def add_task(self, description):
        if not description:
            return None
        if self.tasks_list:
            nuovo_id = max(task["id"] for task in self.tasks_list) + 1
        else:
            nuovo_id = 1
        new_task = {
            "id": nuovo_id,
            "description": description,
            "status": "todo",
            "created_at": self.now_iso(),
            "updated_at": self.now_iso(),
        }
        self.tasks_list.append(new_task)
        write_tasks(self.tasks_list)
        return new_task

    def list_tasks(self, status_filter=None):
        if status_filter:
            return [task for task in self.tasks_list if task["status"] == status_filter]
        return self.tasks_list

    def update_task(self, task_id, new_description):
        task_to_update = self.get_task(task_id)
        if task_to_update:
            task_to_update["description"] = new_description
            task_to_update["updated_at"] = self.now_iso()
            write_tasks(self.tasks_list)
            return True
        return False

    def mark_in_progress(self, task_id):
        task_to_update = self.get_task(task_id)
        if task_to_update:
            task_to_update["status"] = "in-progress"
            task_to_update["updated_at"] = self.now_iso()
            write_tasks(self.tasks_list)
            return True
        return False

    def mark_done(self, task_id):
        task_to_update = self.get_task(task_id)
        if task_to_update:
            task_to_update["status"] = "done"
            task_to_update["updated_at"] = self.now_iso()
            write_tasks(self.tasks_list)
            return True
        return False

    def delete_task(self, task_id):
        task_to_delete = self.get_task(task_id)
        if task_to_delete:
            self.tasks_list.remove(task_to_delete)
            write_tasks(self.tasks_list)
            return True
        return False
