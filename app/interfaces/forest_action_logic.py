from abc import ABCMeta, abstractmethod
from typing import List


class IForestActionLogic(metaclass=ABCMeta):
    @abstractmethod
    def save(forestry_data: dict):
        ...

    @abstractmethod
    def getAll() -> List[dict]:
        ...
