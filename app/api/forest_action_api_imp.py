from flask import Blueprint, request, jsonify
from flask import Response

from pydantic.error_wrappers import ValidationError

from app.logic.forest_action_logic import ForestActionLogic

forest_action_api = Blueprint('forest_action_api', __name__)


@forest_action_api.route("/forest-action",  methods=['GET'])
def getAll():
    forest_actions = ForestActionLogic.getAll()
    return jsonify(forest_actions)


@forest_action_api.route("/forest-action",  methods=['POST'])
def save():
    content = request.json

    try:
        ForestActionLogic.save(content)
    except ValidationError as e:
        return Response(f"{e.json()}", 400)

    return jsonify({'Message': 'Success'})
