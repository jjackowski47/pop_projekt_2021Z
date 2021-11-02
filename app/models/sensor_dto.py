from typing import Literal, Optional
from pydantic import BaseModel
from pydantic.types import UUID1


class Coordinates(BaseModel):
    x: float
    y: float


class SensorDto(BaseModel):
    id: Optional[UUID1]
    location: Coordinates
    type: Literal['FIRE', 'HUMIDITY']
    model: Optional[str] = 'SM-2000'
