# app/models/task.py

class Task:
    """Domain model for a Task, with id, title, description, and completed status."""
    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def to_dict(self):
        """Serialize Task object to a dictionary (for JSON serialization)."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }