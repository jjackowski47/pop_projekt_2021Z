from abc import ABCMeta, abstractmethod
from typing import List
from pydantic.types import UUID1


class ISensorLogic(metaclass=ABCMeta):
    @abstractmethod
    def save(sensor_data: dict) -> UUID1:
        ...

    @abstractmethod
    def getAll() -> List[dict]:
        ...