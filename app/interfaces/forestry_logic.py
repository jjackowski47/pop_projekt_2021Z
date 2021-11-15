from abc import ABCMeta, abstractmethod
from typing import List
from pydantic.types import UUID1


class IForestryLogic(metaclass=ABCMeta):
    @abstractmethod
    def save(forestry_data: dict) -> UUID1:
        ...

    @abstractmethod
    def getAll() -> List[dict]:
        ...