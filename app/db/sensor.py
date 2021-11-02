from app.database import Database
from app.interfaces.sensor_dao import SensorDao
from app.models.sensor_dto import SensorDto


class Sensor(SensorDao):
    def save(sensor_dto: SensorDto):
        with Database() as db:
            return db.execute(f"INSERT INTO sensor(location, type, model) VALUES ('({sensor_dto.location.x},{sensor_dto.location.y})', '{sensor_dto.type}', '{sensor_dto.model}')")

    def getAll():
        with Database() as db:
            return db.query('SELECT * FROM sensor')
