from application.services.use_cases.create_task import CreateTask
from application.services.use_cases.read_task import ReadTask
from application.services.use_cases.update_task import UpdateTask
from application.services.use_cases.delete_task import DeleteTask

class MemoryStorageAdapter:
    def __init__(self):
        self.tasks = {}
        self.task_id_counter = 1

    def save(self, task):
        task.task_id = str(self.task_id_counter)
        self.tasks[task.task_id] = task
        self.task_id_counter += 1
        return task

    def find_by_id(self, task_id):
        return self.tasks.get(task_id)

    def delete(self, task):
        del self.tasks[task.task_id]