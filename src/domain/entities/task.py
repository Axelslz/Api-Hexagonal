class Task:
    def __init__(self, task_id, description, completed=False):
        self.task_id = task_id
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'description': self.description,
            'completed': self.completed
        }
    