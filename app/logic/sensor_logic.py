from pydantic.error_wrappers import ValidationError

from app.interfaces.sensor_logic import ISensorLogic
from app.models.sensor_dto import SensorDto
from app.models.assign_dto import AssignDto
from app.models.message import Message
from app.dao_imp.sensor_dao_imp import SensorDaoImp
from app.dao_imp.forestry_dao_imp import ForestryDaoImp


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

    def assignToForestry(assign_data: dict) -> Message:
        try:
            assign_dto = AssignDto(**assign_data)
        except ValidationError:
            raise

        if not ForestryDaoImp.forestryExistsById(assign_dto.forestry_id):
            return Message(content="Forestry does not exists", code=404)

        if not SensorDaoImp.sensorExistsById(assign_dto.sensor_id):
            return Message(content="Sensor does not exists", code=404)

        SensorDaoImp.setForestryForSensor(
            sensorId=str(assign_dto.sensor_id), forestryId=str(assign_dto.forestry_id))
        return Message(content=f"Sensor {assign_dto.sensor_id} successfully assigned to forestry {assign_dto.forestry_id}", code=200)

    def save(sensor_data: dict):
        try:
            sensor_dto = SensorDto(**sensor_data)
        except ValidationError:
            raise

        return SensorDaoImp.save(sensor_dto)

    def getAll():
        sensors = SensorDaoImp.getAll()
        return list(f.dict() for f in sensors)