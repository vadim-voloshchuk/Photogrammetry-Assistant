from flask_restful import Resource
from flask import jsonify
import time

# Пример структуры пайплайна
PIPELINE = {
    "nodes": [
        {"id": "method_1", "name": "Стереофотограмметрия", "description": "Метод, основанный на использовании пары изображений для получения трехмерной модели объекта."},
        {"id": "method_2", "name": "Лазерное сканирование", "description": "Технология, использующая лазерные лучи для создания точной модели объектов и окружающей среды."},
        {"id": "method_3", "name": "Фотографическая реконструкция", "description": "Метод, при котором множество фотографий комбинируются для создания 3D-объектов."}
    ],
    "edges": [
        {"source": "method_1", "target": "method_3", "properties": {"execution_time": "15s", "ram_usage": "512MB", "cpu_usage": "40%"}},
        {"source": "method_2", "target": "method_3", "properties": {"execution_time": "20s", "ram_usage": "1GB", "cpu_usage": "60%"}},
        {"source": "method_1", "target": "method_2", "properties": {"execution_time": "25s", "ram_usage": "2GB", "cpu_usage": "70%"}}
    ]
}

# Структура для текущего статуса пайплайна
PIPELINE_STATUS = {
    "current_step": "Стереофотограмметрия",
    "progress_percentage": 45,
    "logs": ["Инициализация...", "Обработка данных..."]
}

# Статус пайплайна (для запуска)
PIPELINE_RUNNING = False

class Pipeline(Resource):
    def get(self):
        """Получить пайплайн обработки для задачи"""
        return jsonify(PIPELINE)

class PipelineStatus(Resource):
    def get(self):
        """Получить статус выполнения пайплайна"""
        return jsonify(PIPELINE_STATUS)

class StartPipeline(Resource):
    def post(self):
        """Запустить пайплайн обработки данных"""
        global PIPELINE_RUNNING
        if PIPELINE_RUNNING:
            return jsonify({"error": "500 Internal Server Error", "message": "Пайплайн уже запущен."}), 500
        PIPELINE_RUNNING = True

        # Симуляция выполнения пайплайна
        time.sleep(5)  # Симуляция выполнения
        PIPELINE_STATUS["progress_percentage"] = 100
        PIPELINE_STATUS["current_step"] = "Фотографическая реконструкция"
        PIPELINE_STATUS["logs"].append("Обработка завершена.")

        return jsonify({"message": "Пайплайн запущен", "status": "running"})

class Results(Resource):
    def get(self):
        """Получить результаты обработки"""
        return jsonify({
            "task_id": 1,
            "output": [
                {"name": "3D модель", "type": "model", "url": "/static/models/3d_model.obj"},
                {"name": "Облако точек", "type": "point_cloud", "url": "/static/point_cloud/point_cloud.ply"}
            ]
        })

class Images(Resource):
    def get(self):
        """Получить изображения для загрузки"""
        return jsonify({
            "images": [
                {"url": "/static/images/img1_thumb.jpg", "name": "Изображение 1"},
                {"url": "/static/images/img2_thumb.jpg", "name": "Изображение 2"},
                {"url": "/static/images/img3_thumb.jpg", "name": "Изображение 3"}
            ]
        })
