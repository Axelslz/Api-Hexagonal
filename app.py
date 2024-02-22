from flask import Flask
from dependencies.dependency_injector import configure_dependencies
from routes.task_routes import configure_routes

app = Flask(__name__)

dependencies = configure_dependencies()
task_controller = dependencies['task_controller']
http_adapter = dependencies['http_adapter']

configure_routes(app, task_controller)

if __name__ == '__main__':
    app.run(debug=True)