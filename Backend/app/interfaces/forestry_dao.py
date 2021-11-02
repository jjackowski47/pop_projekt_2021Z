from abc import ABCMeta, abstractmethod

from pydantic.types import UUID1
from models.forestry_dto import ForestryDto


class ForestryDao(metaclass=ABCMeta):
    @abstractmethod
    def save(forestryDto: ForestryDto):
        ...

    @abstractmethod
    def getAll():
        ...

    @abstractmethod
    def existsById(id: UUID1) -> bool:
        ...
