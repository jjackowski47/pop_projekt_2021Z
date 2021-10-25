from datetime import datetime
from sqlalchemy.orm.session import Session
from models.db import Forestry
from flask import Blueprint, request, jsonify, Response

from pydantic.error_wrappers import ValidationError

from database import get_db
from models.db import Sensor

db: Session = next(get_db())

forestry_api = Blueprint('forestry_api', __name__)


@forestry_api.route("/forestry",  methods=['GET'])
def get_all_forestries():
    db.add(Sensor(location='POINT(4 1)',
           type="as", model="asdasd"))
    db.commit()
    return f"{db.query(Sensor).all()}"


@ forestry_api.route("/forestry",  methods=['POST'])

def save_forestry():
    content = request.json

    try:
        Forestry(**content)
    except ValidationError as e:
        return Response(f"{e.json()}", 400)

    forestry_id = content.get('id', None)
    location = content.get('location', None)
    name = content.get('name', None)

    """TODO save forestry in DB via ForestryDao"""

    return jsonify(content)
