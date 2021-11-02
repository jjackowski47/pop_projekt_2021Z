from flask import Blueprint, request, jsonify
from flask import Response

from pydantic.error_wrappers import ValidationError

from models.forestry_dto import ForestryDto
from db.forestry import Forestry


forestry_api = Blueprint('forestry_api', __name__)


@forestry_api.route("/forestry",  methods=['GET'])
def get_all_forestries():
    forestries_data: ForestryDto = Forestry.getAll()
    return jsonify(forestries_data)


@forestry_api.route("/forestry",  methods=['POST'])
def save_forestry():
    content = request.json
    print(content)
    try:
        forestry_dto = ForestryDto(**content)
    except ValidationError as e:
        return Response(f"{e.json()}", 400)

    Forestry.save(forestry_dto)

    return jsonify("Success")
