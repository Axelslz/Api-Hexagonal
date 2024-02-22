class UpdateTask:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, task_id, new_description):
        task = self.task_repository.find_by_id(task_id)

        if task:
            task.description = new_description
            updated_task = self.task_repository.save(task)
            return updated_task
        else:
            return None