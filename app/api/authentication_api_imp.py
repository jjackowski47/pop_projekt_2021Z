from flask import Blueprint

from app.logic.authentication_logic import AuthenticationLogic


authentication_api = Blueprint('authentication_api', __name__)


@authentication_api.route("/token",  methods=['GET'])
def generateToken():
    token = AuthenticationLogic.generateToken()
    return str(token), 200


def isValid(token: str):
    return AuthenticationLogic.isValid(token)
