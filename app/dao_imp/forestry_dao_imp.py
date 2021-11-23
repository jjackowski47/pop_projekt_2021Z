from pydantic.types import UUID1
from app.interfaces.forestry_dao import ForestryDao
from app.models.forestry_dto import ForestryDto, Coordinates
from app.database import Database
import re


class ForestryDaoImp(ForestryDao):

    def save(forestry_dto: ForestryDto):
        with Database() as db:
            polygon_string = coordinatesToPolygonString(forestry_dto.location)
            forestry_row = db.ForestryRow(
                name=forestry_dto.name, location=polygon_string)
            db.session.add(forestry_row)
            db.session.commit()
            return forestry_row.id

    def get(id: UUID1):
        with Database() as db:
            forestry_row = db.session.query(db.ForestryRow).filter(
                db.ForestryRow.id == id.hex).first()
            coordinates = polygonStringToCoordinates(
                str(forestry_row.location))
            return ForestryDto(id=forestry_row.id, name=forestry_row.name, location=coordinates)

    def getAll():
        with Database() as db:
            forestries_dtos = []
            for forestry_row in db.session.query(db.ForestryRow).all():
                coordinates = polygonStringToCoordinates(
                    str(forestry_row.location))
                forestries_dtos.append(ForestryDto(
                    id=forestry_row.id, name=forestry_row.name, location=coordinates))
            return forestries_dtos

    def delete(id: UUID1):
        with Database() as db:
            forestry = db.session.query(db.ForestryRow).filter(
                db.ForestryRow.id == id.hex).first()
            db.session.delete(forestry)

    def update(forestry_dto: ForestryDto):
        with Database() as db:
            forestry_row = db.session.query(db.ForestryRow).filter(
                db.ForestryRow.id == forestry_dto.id.hex).first()
            forestry_row.name = forestry_dto.name
            polygon_string = coordinatesToPolygonString(forestry_dto.location)
            forestry_row.location = polygon_string

    def existsById(id: UUID1) -> bool:
        pass


def polygonStringToCoordinates(polygonString: str):
    list_of_floats = re.findall(r'[\d.-]+', polygonString)
    coordinates = []
    for i in range(0, len(list_of_floats), 2):
        coor = Coordinates(long=list_of_floats[i], lat=list_of_floats[i+1])
        coordinates.append(coor)
    return coordinates


def coordinatesToPolygonString(coordinates):
    return ','.join([f'({coord.long}, {coord.lat})' for coord in coordinates])