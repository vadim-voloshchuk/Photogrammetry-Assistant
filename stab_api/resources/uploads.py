import os
import base64
import json
from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename

# Пример пути для хранения загруженных изображений
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

# Функция для проверки поддерживаемых расширений изображений
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Модель данных для загрузки
class UploadData(Resource):
    def post(self):
        # Получаем данные из тела запроса
        data = request.get_json()

        # Проверяем обязательные поля
        if not data.get('task_id') or not data.get('image_files') or not data.get('text'):
            return {"error": "400 Bad Request", "message": "Необходимо указать параметры task_id, text и хотя бы одно изображение для загрузки."}, 400

        task_id = data['task_id']
        image_files = data['image_files']
        text = data['text']

        # Папка для хранения изображений
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        uploaded_images = []

        # Обрабатываем список изображений
        for i, image_data in enumerate(image_files):
            try:
                # Декодируем base64 изображение
                img_data = base64.b64decode(image_data)
                filename = f"{task_id}_image_{i + 1}.jpg"  # Генерируем имя файла

                # Проверяем расширение
                if not allowed_file(filename):
                    return {"error": "415 Unsupported Media Type", "message": "Неподдерживаемый формат изображения. Пожалуйста, загрузите изображения в формате .jpg, .png, .jpeg."}, 415

                # Сохраняем изображение в файл
                file_path = os.path.join(UPLOAD_FOLDER, secure_filename(filename))
                with open(file_path, 'wb') as f:
                    f.write(img_data)

                # Добавляем информацию о загруженном изображении в список
                uploaded_images.append({
                    "filename": filename,
                    "status": "uploaded",
                    "size": f"{os.path.getsize(file_path) / (1024 * 1024):.2f}MB"  # Размер в мегабайтах
                })

            except Exception as e:
                return {"error": "500 Internal Server Error", "message": f"Произошла ошибка при загрузке изображения: {str(e)}."}, 500

        # Статус задачи (например, "processing", можно изменить в зависимости от логики приложения)
        status = "processing"

        return {
            "message": "Данные успешно загружены",
            "task_id": task_id,
            "status": status,
            "uploaded_images": uploaded_images
        }, 200
