from flask import Flask, request, jsonify
from controllers.task_controller import TaskController

def configure_routes(app, task_controller):
    @app.route('/tasks', methods=['POST'])
    def create_task():
        return task_controller.create_task()

    @app.route('/tasks/<task_id>', methods=['GET'])
    def read_task(task_id):
        return task_controller.read_task(task_id)

    @app.route('/tasks/<task_id>', methods=['PUT'])
    def update_task(task_id):
        return task_controller.update_task(task_id)

    @app.route('/tasks/<task_id>', methods=['DELETE'])
    def delete_task(task_id):
        return task_controller.delete_task(task_id)