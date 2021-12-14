from abc import ABCMeta, abstractmethod
from typing import List
from pydantic.types import UUID1


class AuthenticationDao(metaclass=ABCMeta):
    @abstractmethod
    def generateToken():
        ...

    @abstractmethod
    def isValid(token: str):
        ...
