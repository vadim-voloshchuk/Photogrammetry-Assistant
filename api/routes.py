from flask import Blueprint, request, jsonify
import time

api_bp = Blueprint('api', __name__)

# Список задач для выбора
tasks = [
    {"id": 1, "name": "3D моделирование", "description": "Создание 3D модели из фотографий", "icon": "3d_icon.png"},
    {"id": 2, "name": "Измерение расстояний", "description": "Определение расстояний между объектами", "icon": "distance_icon.png"},
    {"id": 3, "name": "Создание ортофотопланов", "description": "Создание ортофотопланов с высокоточной геометрией", "icon": "ortho_icon.png"}
]

# Структура пайплайна (стаб)
pipeline = {
    "task_id": 1,
    "steps": [
        {"name": "Сбор данных", "description": "Сбор фотографий и метаданных", "input": "Фотографии", "output": "Преобразованные данные"},
        {"name": "Калибровка камеры", "description": "Определение параметров камеры", "input": "Фотографии", "output": "Калиброванные фотографии"},
        {"name": "Стереообработка", "description": "Создание облака точек", "input": "Калиброванные фотографии", "output": "Облако точек"}
    ]
}

# Прогресс выполнения (стаб)
progress = {
    "current_step": "Стереообработка",
    "progress_percentage": 45,  # Процент завершения
    "logs": ["Инициализация...", "Обработка данных..."]
}

# Результаты (стаб)
results = {
    "task_id": 1,
    "output": [
        {"name": "3D модель", "type": "model", "url": "/static/models/3d_model.obj"},
        {"name": "Облако точек", "type": "point_cloud", "url": "/static/point_cloud/point_cloud.ply"}
    ]
}

# Эндпоинт для получения задач
@api_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# Эндпоинт для загрузки данных
@api_bp.route('/upload', methods=['POST'])
def upload_data():
    data = request.json
    # Фиктивная логика для обработки данных
    task_id = data.get('task_id')
    camera_type = data.get('camera_type')
    resolution = data.get('resolution')
    focal_length = data.get('focal_length')
    lighting_conditions = data.get('lighting_conditions')
    gps_data = data.get('gps_data')

    # Здесь можно добавить логику обработки и хранения данных, пока просто стаб
    return jsonify({"message": "Данные успешно загружены", "task_id": task_id})

# Эндпоинт для получения пайплайна
@api_bp.route('/pipeline', methods=['GET'])
def get_pipeline():
    return jsonify(pipeline)

# Эндпоинт для получения статуса пайплайна
@api_bp.route('/pipeline/status', methods=['GET'])
def get_pipeline_status():
    # Можно добавить логику, которая будет обновлять progress в реальном времени
    return jsonify(progress)

# Эндпоинт для запуска пайплайна (стаб)
@api_bp.route('/pipeline/start', methods=['POST'])
def start_pipeline():
    # Стаб для имитации выполнения пайплайна
    time.sleep(2)  # Имитация выполнения пайплайна (например, через время)
    progress["current_step"] = "Завершено"
    progress["progress_percentage"] = 100
    progress["logs"].append("Пайплайн завершен!")
    return jsonify({"message": "Пайплайн запущен", "status": "running"})

# Эндпоинт для получения результатов
@api_bp.route('/results', methods=['GET'])
def get_results():
    return jsonify(results)

# Эндпоинт для получения изображений (миниатюр), используемых для загрузки (стаб)
@api_bp.route('/images', methods=['GET'])
def get_images():
    # Здесь можно вернуть список миниатюр изображений для предварительного просмотра
    image_preview = [
        {"url": "/static/images/img1_thumb.jpg", "name": "Изображение 1"},
        {"url": "/static/images/img2_thumb.jpg", "name": "Изображение 2"},
        {"url": "/static/images/img3_thumb.jpg", "name": "Изображение 3"}
    ]
    return jsonify({"images": image_preview})

# Эндпоинт для получения информации о камере (стаб)
@api_bp.route('/camera-types', methods=['GET'])
def get_camera_types():
    camera_types = [
        {"id": 1, "name": "Canon EOS 5D", "focal_lengths": [24, 50, 85]},
        {"id": 2, "name": "Nikon D850", "focal_lengths": [35, 70, 200]},
        {"id": 3, "name": "Sony Alpha 7R", "focal_lengths": [28, 50, 100]}
    ]
    return jsonify({"camera_types": camera_types})

# Эндпоинт для получения списка условий съемки (стаб)
@api_bp.route('/lighting-conditions', methods=['GET'])
def get_lighting_conditions():
    conditions = [
        {"id": 1, "name": "Солнечно"},
        {"id": 2, "name": "Облачно"},
        {"id": 3, "name": "Тень"},
        {"id": 4, "name": "Ночной съемки"}
    ]
    return jsonify({"lighting_conditions": conditions})

# Эндпоинт для получения GPS-данных (стаб)
@api_bp.route('/gps-data', methods=['POST'])
def upload_gps_data():
    gps_file = request.files['file']
    # Здесь можно добавить обработку загруженного GPS-файла
    return jsonify({"message": "GPS данные успешно загружены", "file_name": gps_file.filename})

# Эндпоинт для получения и добавления логов выполнения
@api_bp.route('/logs', methods=['GET', 'POST'])
def manage_logs():
    if request.method == 'POST':
        log_entry = request.json.get('log_entry')
        progress["logs"].append(log_entry)
        return jsonify({"message": "Лог добавлен", "logs": progress["logs"]})
    return jsonify({"logs": progress["logs"]})

