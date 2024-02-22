from flask import Flask, request, jsonify
from application.services.use_cases.create_task import CreateTask
from application.services.use_cases.read_task import ReadTask
from application.services.use_cases.update_task import UpdateTask
from application.services.use_cases.delete_task import DeleteTask

class TaskController:
    def __init__(self, create_task_service, read_task_service, update_task_service, delete_task_service):
        self.create_task_service = create_task_service
        self.read_task_service = read_task_service
        self.update_task_service = update_task_service
        self.delete_task_service = delete_task_service

    def create_task(self):
        data = request.get_json()
        description = data.get('description')

        if description:
            created_task = self.create_task_service.execute(description)
            return jsonify(created_task.to_dict()), 201
        else:
            return jsonify({'error': 'Description is required'}), 400

    def read_task(self, task_id):
        task = self.read_task_service.execute(task_id)
        if task:
            return jsonify(task.to_dict())
        else:
            return jsonify({'error': 'Task not found'}), 404

    def update_task(self, task_id):
        data = request.get_json()
        new_description = data.get('description')

        if new_description:
            updated_task = self.update_task_service.execute(task_id, new_description)
            if updated_task:
                return jsonify(updated_task.to_dict())
            else:
                return jsonify({'error': 'Task not found'}), 404
        else:
            return jsonify({'error': 'New description is required'}), 400

    def delete_task(self, task_id):
        success = self.delete_task_service.execute(task_id)
        if success:
            return jsonify({'message': 'Task deleted successfully'}), 200
        else:
            return jsonify({'error': 'Task not found'}), 404