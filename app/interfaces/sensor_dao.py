from abc import ABCMeta, abstractmethod
from app.models.sensor_dto import SensorDto
from pydantic.types import UUID1

class SensorDao(metaclass=ABCMeta):

    @abstractmethod
    def save(sensor_dto: SensorDto):
        ...

    @abstractmethod
    def getAll():
        ...

    @abstractmethod
    def sensorExistById(id: UUID1) -> bool:
        ...

    @abstractmethod
    def setForestryForSensor(sensorId: UUID1, forestryId: UUID1):
        ...