from abc import ABCMeta, abstractmethod
from typing import List
from pydantic.types import UUID1


class IAuthenticationLogic(metaclass=ABCMeta):
    @abstractmethod
    def generateToken() -> str:
        ...

    @abstractmethod
    def isValid(token: str) -> bool:
        ...
