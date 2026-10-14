"""Core logic: add, list, complete and remove tasks. Data is stored in a JSON file."""
import json
from pathlib import Path

DEFAULT_FILE = Path("tasks.json")


def load_tasks(path=DEFAULT_FILE):
    path = Path(path)
    if not path.exists():
        return []
    return json.loads(path.read_text())


def save_tasks(tasks, path=DEFAULT_FILE):
    Path(path).write_text(json.dumps(tasks, indent=2))


def add_task(tasks, title):
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty")
    task = {"id": max((t["id"] for t in tasks), default=0) + 1,
            "title": title,
            "done": False}
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    raise KeyError(f"No task with id {task_id}")


def remove_task(tasks, task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            return tasks.pop(i)
    raise KeyError(f"No task with id {task_id}")
