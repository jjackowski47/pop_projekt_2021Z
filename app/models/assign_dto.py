from pydantic import BaseModel
from pydantic.types import UUID1


class AssignDto(BaseModel):
    forestry_id: UUID1
    sensor_id: UUID1
