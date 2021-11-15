from pydantic.types import UUID1

from app.database import Database
from app.interfaces.sensor_dao import SensorDao
from app.models.sensor_dto import SensorDto, Coordinates

import re


class SensorDaoImp(SensorDao):

    def save(sensor_dto: SensorDto):
        with Database() as db:
            pointString = coordinateToPointString(sensor_dto.location)
            sensor_row = db.SensorRow(location=pointString, type=sensor_dto.type, model=sensor_dto.model)
            db.session.add(sensor_row)
            db.session.commit()
            return sensor_row.id

    def get(id: UUID1):
        with Database() as db:
            sensor_row = db.session.query(db.SensorRow).filter(db.SensorRow.id == id.hex).first()
            point = pointStringToCoordinate(str(sensor_row.location))
            return SensorDto(id=sensor_row.id, location=point, type=sensor_row.type, model=sensor_row.model)

    def getAll():
        with Database() as db:
            return db.query('SELECT * FROM sensor')

        sensors_dtos = []

        for sensor_row in db.session.query(db.SensorRow).all():
            point = pointStringToCoordinate(str(sensor_row.location))
            sensors_dtos.append(SensorDto(id=sensor_row.id, location=point, type=sensor_row.type, model=sensor_row.model))
        return sensors_dtos

    def delete(id: UUID1):
        pass

    def update(sensor_dto: SensorDto):
        pass

    def addReadingsLog(sensorLog_dto):
        pass

    def getReadingsLog(id: UUID1):
        pass

    def getAllReadingsLogs():
        pass

    def deleteReadingsLog(id: UUID1):
        pass

    def addEmergencyEvent(emergencyEvent_dto):
        pass

    def getEmergencyEvent(id: UUID1):
        pass

    def getAllEmergencyEvents():
        pass

    def deleteEmergencyEvent(id: UUID1):
        pass

def pointStringToCoordinate(pointString : str):
    points = re.findall(r'[\d.-]+', pointString)
    return Coordinates(x=points[0], y=points[1])

def coordinateToPointString(coordinate):
    return f'({coordinate.x}, {coordinate.y})'