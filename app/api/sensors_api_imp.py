from flask import Blueprint, request, jsonify
from flask import Response

from pydantic.error_wrappers import ValidationError

from app.models.message import Message
from app.logic.sensor_logic import SensorLogic

sensor_api = Blueprint('sensor_api', __name__)


@sensor_api.route("/sensor",  methods=['GET'])
def getAll():
    sensors = SensorLogic.getAll()
    return jsonify(sensors)


@sensor_api.route("/assign",  methods=['POST'])
def assignToForestry():
    content = request.json

    message: Message = SensorLogic.assignToForestry(content)

    return Response(message.content, content_type="application/json", status=message.code)
