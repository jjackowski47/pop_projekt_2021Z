from flask import Blueprint, request, jsonify
from flask import Response

from pydantic.error_wrappers import ValidationError

from models.forestry import Forestry


forestry_api = Blueprint('forestry_api', __name__)


@forestry_api.route("/forestry",  methods=['GET'])
def get_all_forestries():
    """TODO get all forestries in DB via ForestryDao"""

    pass


@forestry_api.route("/forestry",  methods=['POST'])
def save_forestry():
    content = request.json
    print(content)
    try:
        Forestry(**content)
    except ValidationError as e:
        return Response(f"{e.json()}", 400)

    forestry_id = content.get('id', None)
    location = content.get('location', None)
    name = content.get('name', None)

    """TODO save forestry in DB via ForestryDao"""

    return jsonify(content)
