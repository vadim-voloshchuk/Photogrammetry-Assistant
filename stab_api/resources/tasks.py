from flask import request, jsonify
from flask_restful import Resource

# Заглушки данных
tasks_data = [
    {
        "id": 1,
        "name": "3D моделирование",
        "description": "Создание 3D модели из фотографий",
        "icon": "3d_icon.png",
        "category": "3D моделирование",
        "difficulty": "medium",
        "priority": 3,
        "estimated_time": "3h",
        "tags": ["моделирование", "фотограмметрия"],
        "created_at": "2024-11-01T12:00:00Z",
        "updated_at": "2024-11-02T15:30:00Z"
    },
    {
        "id": 2,
        "name": "Измерение расстояний",
        "description": "Определение расстояний между объектами",
        "icon": "distance_icon.png",
        "category": "Геодезия",
        "difficulty": "easy",
        "priority": 2,
        "estimated_time": "1h",
        "tags": ["анализ", "геодезия"],
        "created_at": "2024-10-25T09:00:00Z",
        "updated_at": "2024-10-26T10:15:00Z"
    }
]

class Tasks(Resource):
    def get(self):
        return jsonify({"tasks": tasks_data})

class CreateTask(Resource):
    def post(self):
        task = request.get_json()
        task_id = len(tasks_data) + 1
        task['id'] = task_id
        tasks_data.append(task)
        return jsonify({"message": "Задача успешно создана", "task": task})

class UpdateTask(Resource):
    def put(self, task_id):
        task = request.get_json()
        for t in tasks_data:
            if t['id'] == task_id:
                t.update(task)
                return jsonify({"message": "Задача успешно обновлена", "task": t})
        return jsonify({"error": "404 Not Found", "message": "Задача не найдена"}), 404

class DeleteTask(Resource):
    def delete(self, task_id):
        global tasks_data
        tasks_data = [t for t in tasks_data if t['id'] != task_id]
        return jsonify({"message": "Задача успешно удалена"})

class UploadData(Resource):
    def post(self):
        data = request.get_json()
        task_id = data.get("task_id")
        status = "queued"
        return jsonify({
            "message": "Данные успешно загружены",
            "task_id": task_id,
            "status": status,
            "uploaded_images": [{"filename": img, "status": "uploaded", "size": "2MB"} for img in data.get("image_files", [])]
        })
