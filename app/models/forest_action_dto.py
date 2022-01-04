from typing import List, Literal, Optional
from pydantic import BaseModel, validator, root_validator
from pydantic.types import UUID1, confloat, conlist
from datetime import date


class Coordinates(BaseModel):
    long: confloat(ge=-180.0, le=180.0)
    lat: confloat(ge=-180.0, le=180.0)

    def __hash__(self):
        return hash((self.long, self.lat))


class ForestActionDto(BaseModel):
    id: Optional[UUID1]
    location: conlist(Coordinates, min_items=3)
    type: Literal['DEFORESTRATION', 'AFORESTRATION']
    subtype: Optional[str]
    begin: date
    end: date
    forestry_id: UUID1

    @validator('location')
    def coords_create_polygon(cls, value: List[Coordinates]):
        if len(set(value)) < 3:
            raise ValueError(
                "Invalid coordinates: coordinates cannot form proper polygon")
        return value

    @root_validator
    def subtype_required_if_type_DEFORESTRATION(cls, values):
        if values.get('type') == 'DEFORESTRATION':
            subtype = values.get('subtype')
            assert subtype is not None and len(values.get(
                'subtype')) > 0, 'subtype required for type DEFORESTRATION'
        return values

    @root_validator
    def begin_before_end(cls, values):
        begin, end = values.get('begin'), values.get('end')
        if begin is not None and end is not None and begin > end:
            raise ValueError('End datetime must happen after begin datetime')
        return values
