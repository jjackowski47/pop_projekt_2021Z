from flask import Blueprint, request, jsonify
from flask import Response

from pydantic.error_wrappers import ValidationError

from db.sensor import Sensor
from models.sensor_dto import SensorDto


sensor_api = Blueprint('sensor_api', __name__)


@sensor_api.route("/sensor",  methods=['GET'])
def get_all_sensors():
    sensors_data: SensorDto = Sensor.getAll()
    sensors_data_as_objects = map(transformSensorsArrayToObject, sensors_data)
    return jsonify(list(sensors_data_as_objects))


@sensor_api.route("/sensor",  methods=['POST'])
def register_sensor():
    content = request.json

    try:
        sensor_dto = SensorDto(**content)
    except ValidationError as e:
        return Response(f"{e.json()}", 400)

    Sensor.save(sensor_dto)

    return jsonify("Success")


def transformSensorsArrayToObject(arr):
        return {'id': arr[0], 'location': arr[1], 'type': arr[2], 'model': arr[3]}
