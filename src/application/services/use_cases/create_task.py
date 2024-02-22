from domain.entities.task import Task

class CreateTask:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, description):
        task = Task(task_id=None, description=description)
        created_task = self.task_repository.save(task)
        return created_task