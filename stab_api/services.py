from flask import request

@api_bp.route('/upload', methods=['POST'])
def upload_data():
    task_id = request.json.get('task_id')
    camera_type = request.json.get('camera_type')
    resolution = request.json.get('resolution')
    focal_length = request.json.get('focal_length')
    lighting_conditions = request.json.get('lighting_conditions')
    gps_data = request.json.get('gps_data')

    # Здесь можно добавить логику обработки и хранения данных
    return jsonify({"message": "Данные успешно загружены", "task_id": task_id})
