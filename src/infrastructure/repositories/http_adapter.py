from flask import Flask, request, jsonify
from application.services.use_cases.create_task import CreateTask
from application.services.use_cases.read_task import ReadTask
from application.services.use_cases.update_task import UpdateTask
from application.services.use_cases.delete_task import DeleteTask

app = Flask(__name__)

class HTTPAdapter:
    def __init__(self, create_task_service, read_task_service, update_task_service, delete_task_service):
        self.create_task_service = create_task_service
        self.read_task_service = read_task_service
        self.update_task_service = update_task_service
        self.delete_task_service = delete_task_service

    @app.route('/tasks', methods=['POST'])
    def create_task():
        data = request.get_json()
        description = data.get('description')

        if description:
            created_task = HTTPAdapter.create_task_service.execute(description)
            return jsonify(created_task.to_dict()), 201
        else:
            return jsonify({'error': 'Description is required'}), 400

    @app.route('/tasks/<task_id>', methods=['GET'])
    def read_task(task_id):
        task = HTTPAdapter.read_task_service.execute(task_id)
        if task:
            return jsonify(task.to_dict())
        else:
            return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)