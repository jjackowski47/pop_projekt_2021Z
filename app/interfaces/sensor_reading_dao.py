from abc import ABCMeta, abstractmethod
from app.models.sensor_dto import SensorReadingDto

class SensorReadingDao(metaclass=ABCMeta):

    @abstractmethod
    def registerReading(sensor_reading_dto: SensorReadingDto):
        ...
