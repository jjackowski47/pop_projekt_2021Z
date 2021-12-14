from typing import Literal, Optional
from pydantic import BaseModel
from pydantic.types import UUID1, confloat


class Coordinates(BaseModel):
    long: confloat(ge=-180.0, le=180.0)
    lat: confloat(ge=-180.0, le=180.0)

    def __hash__(self):
        return hash((self.long, self.lat))


class SensorDto(BaseModel):
    id: Optional[UUID1]
    location: Coordinates
    type: Literal['FIRE', 'HUMIDITY']
    model: Optional[str] = 'SM-2000'
    forestry_id: Optional[UUID1]

class SensorRegistratorDto(BaseModel):
    sensor_dto: SensorDto
    token: str
