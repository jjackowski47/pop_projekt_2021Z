from pydantic.error_wrappers import ValidationError

from app.interfaces.sensor_logic import ISensorLogic
from app.models.sensor_dto import SensorDto
from app.dao_imp.sensor_dao_imp import SensorDaoImp

class SensorLogic(ISensorLogic):
    def save(sensor_data: dict):
        try:
            sensor_dto = SensorDto(**sensor_data)
        except ValidationError:
            raise

        return SensorDaoImp.save(sensor_dto)

    def getAll():
        sensors = SensorDaoImp.getAll()
        return list(f.dict() for f in sensors)