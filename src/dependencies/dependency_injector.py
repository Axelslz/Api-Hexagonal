from controllers.task_controller import TaskController
from application.services.use_cases.create_task import CreateTask
from application.services.use_cases.read_task import ReadTask
from application.services.use_cases.update_task import UpdateTask
from application.services.use_cases.delete_task import DeleteTask
from infrastructure.repositories.memory_storage_adapter import MemoryStorageAdapter
from infrastructure.repositories.http_adapter import HTTPAdapter

def configure_dependencies():
    memory_storage_adapter = MemoryStorageAdapter()

    create_task_service = CreateTask(memory_storage_adapter)
    read_task_service = ReadTask(memory_storage_adapter)
    update_task_service = UpdateTask(memory_storage_adapter)
    delete_task_service = DeleteTask(memory_storage_adapter)

    http_adapter = HTTPAdapter(
        create_task_service,
        read_task_service,
        update_task_service,
        delete_task_service
    )

    task_controller = TaskController(
        create_task_service,
        read_task_service,
        update_task_service,
        delete_task_service
    )

    return {
        'http_adapter': http_adapter,
        'task_controller': task_controller
    }