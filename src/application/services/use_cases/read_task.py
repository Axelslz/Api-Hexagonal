class ReadTask:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, task_id):
        task = self.task_repository.find_by_id(task_id)
        return task