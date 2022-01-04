from app.dao_imp.forestry_dao_imp import polygonStringToCoordinates, coordinatesToPolygonString
from pydantic.types import UUID1
from app.interfaces.forest_action_dao import ForestActionDao
from app.models.forest_action_dto import ForestActionDto
from app.database import Database

with Database() as db:
    class ForestActionDaoImp(ForestActionDao):

        def getAll():
            forest_action_dtos = []
            for forest_action_row in db.session.query(db.ForestActionRow).all():
                coordinates = polygonStringToCoordinates(
                    str(forest_action_row.location))
                forest_action_dtos.append(
                    ForestActionDto(
                        id=forest_action_row.id,
                        location=coordinates,
                        type=forest_action_row.type,
                        subtype=forest_action_row.subtype,
                        forestry_id=forest_action_row.forestry_id,
                        begin="2022-01-01",
                        end="2022-01-02",
                    )
                )
            return forest_action_dtos

        def save(forestActionDto: ForestActionDto):
            polygon_string = coordinatesToPolygonString(
                forestActionDto.location)
            subtype = forestActionDto.subtype if forestActionDto.subtype else "null"
            forest_action_row = db.ForestActionRow(
                location=polygon_string, type=forestActionDto.type, subtype=subtype, forestry_id=str(
                    forestActionDto.forestry_id)
            )
            db.session.add(forest_action_row)
            db.session.commit()
            return forest_action_row.id
