from flask import Flask
from flask_cors import CORS
from app.api.forestry_api_imp import forestry_api
from app.api.sensors_api_imp import sensor_api
from app.api.sensor_registrator_api_imp import sensor_registrator_api
from app.api.authentication_api_imp import authentication_api


app = Flask(__name__)
app.config["DEBUG"] = True
app.register_blueprint(forestry_api)
app.register_blueprint(sensor_api)
app.register_blueprint(authentication_api)
app.register_blueprint(sensor_registrator_api)
CORS(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
