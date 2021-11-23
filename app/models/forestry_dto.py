from typing import List, Optional
from pydantic import BaseModel, validator
from pydantic.types import UUID1, confloat, conlist, constr


class Coordinates(BaseModel):
    long: confloat(ge=-180.0, le=180.0)
    lat: confloat(ge=-180.0, le=180.0)

    def __hash__(self):
        return hash((self.long, self.lat))


class ForestryDto(BaseModel):
    id: Optional[UUID1]
    location: conlist(Coordinates, min_items=3)
    name: constr(regex=r"^[a-zA-Z0-9\s]+$")

    @validator('location')
    def coords_create_polygon(cls, value: List[Coordinates]):
        if len(set(value)) < 3:
            raise ValueError(
                "Invalid coordinates: coordinates cannot form proper polygon")
        return value