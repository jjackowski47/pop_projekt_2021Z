from abc import ABCMeta, abstractmethod
from app.models.sensor_dto import SensorDto


class SensorDao(metaclass=ABCMeta):

    @abstractmethod
    def save(sensor_dto: SensorDto):
        ...

    @abstractmethod
    def getAll():
        ...
