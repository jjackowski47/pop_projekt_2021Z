from flask import Flask
from app.api.forestry_api import forestry_api
from app.api.sensors_api import sensor_api

app = Flask(__name__)
app.config["DEBUG"] = True
app.register_blueprint(forestry_api)
app.register_blueprint(sensor_api)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
