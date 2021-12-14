from abc import ABCMeta, abstractmethod


class ISensorRegistratorLogic(metaclass=ABCMeta):
    @abstractmethod
    def registerSensor(sensor_data: dict) -> bool:
        ...
