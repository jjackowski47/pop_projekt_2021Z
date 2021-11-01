from flask import Flask
from forestry_api import forestry_api
from sensors_api import sensor_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.register_blueprint(forestry_api)
app.register_blueprint(sensor_api)


if __name__ == "__main__":
    app.run()
