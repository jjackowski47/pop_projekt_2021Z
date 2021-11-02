from typing import Optional
from pydantic import BaseModel
from pydantic.types import UUID1, conlist


class Coordinates(BaseModel):
    x: float
    y: float


class ForestryDto(BaseModel):
    id: Optional[UUID1]
    location: conlist(Coordinates, min_items=3)
    name: str
