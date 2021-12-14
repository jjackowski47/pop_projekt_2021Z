from flask import Blueprint, request, jsonify
from flask import Response

from pydantic.error_wrappers import ValidationError
from app.logic.sensor_registrator_logic import SensorRegistratorLogic

from app.logic.authentication_logic import AuthenticationLogic


sensor_registrator_api = Blueprint('sensor_registrator_api', __name__)


@sensor_registrator_api.route("/register",  methods=['POST'])
def registerSensor():
    content = request.json

    try:
        registered = SensorRegistratorLogic.registerSensor(content)
    except ValidationError as e:
        return Response(f"{e.json()}", 400)

    return jsonify({"registered": registered})
