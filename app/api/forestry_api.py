from flask import Blueprint, request, jsonify
from flask import Response

from pydantic.error_wrappers import ValidationError

from app.models.forestry_dto import ForestryDto
from app.db.forestry import Forestry


forestry_api = Blueprint('forestry_api', __name__)

@forestry_api.route("/forestry",  methods=['GET'])
def get_all_forestries():
    forestries_data: ForestryDto = Forestry.getAll()
    forestries_data_as_objects = map(transformForestriesArrayToObject, forestries_data)
    return jsonify(list(forestries_data_as_objects))


@forestry_api.route("/forestry",  methods=['POST'])
def save_forestry():
    content = request.json

    try:
        forestry_dto = ForestryDto(**content)
    except ValidationError as e:
        return Response(f"{e.json()}", 400)

    Forestry.save(forestry_dto)

    return jsonify("Success")

def transformForestriesArrayToObject(arr):
        return {'id': arr[0], 'location': arr[1], 'name': arr[2]}
