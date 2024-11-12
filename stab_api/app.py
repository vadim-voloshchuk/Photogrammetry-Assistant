from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
import config
from resources.tasks import Tasks, CreateTask, UpdateTask, DeleteTask
from resources.uploads import UploadData
from resources.pipeline import Pipeline, PipelineStatus, StartPipeline, Results, Images  # Новые ресурсы для пайплайна

# Создаем приложение Flask
app = Flask(__name__, static_folder='static')
api = Api(app)

# Настройка Swagger UI
SWAGGER_URL = '/swagger'  # Путь для Swagger UI
API_URL = '/static/swagger.json'

# Регистрируем blueprint для Swagger UI
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Photogrammetry Assistant API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Регистрация ресурсов
api.add_resource(Tasks, '/tasks')
api.add_resource(CreateTask, '/tasks')
api.add_resource(UpdateTask, '/tasks/<int:task_id>')
api.add_resource(DeleteTask, '/tasks/<int:task_id>')
api.add_resource(UploadData, '/upload')
api.add_resource(Pipeline, '/pipeline')
api.add_resource(PipelineStatus, '/pipeline/status')
api.add_resource(StartPipeline, '/pipeline/start')
api.add_resource(Results, '/results')
api.add_resource(Images, '/images')

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
