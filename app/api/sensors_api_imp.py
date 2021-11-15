from flask import Blueprint, request, jsonify
from flask import Response

from pydantic.error_wrappers import ValidationError

from app.logic.sensor_logic import SensorLogic

sensor_api = Blueprint('sensor_api', __name__)


@sensor_api.route("/sensor",  methods=['GET'])
def getAll():
    sensors = SensorLogic.getAll()
    return jsonify(sensors)


@sensor_api.route("/sensor",  methods=['POST'])
def registerSensor():
    content = request.json

    try:
        id = SensorLogic.save(content)
    except ValidationError as e:
        return Response(f"{e.json()}", 400)

    return jsonify({'Message': 'Success', 'Sensor_id': id})