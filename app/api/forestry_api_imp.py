from flask import Blueprint, request, jsonify
from flask import Response

from pydantic.error_wrappers import ValidationError

from app.logic.forestry_logic import ForestryLogic

forestry_api = Blueprint('forestry_api', __name__)


@forestry_api.route("/forestry",  methods=['GET'])
def getAll():
    forestries = ForestryLogic.getAll()
    return jsonify(forestries)


@forestry_api.route("/forestry",  methods=['POST'])
def save():
    content = request.json

    try:
        id = ForestryLogic.save(content)
    except ValidationError as e:
        return Response(f"{e.json()}", 400)

    return jsonify({'Message': 'Success', 'Forestry_id': id})