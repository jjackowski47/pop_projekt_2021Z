from pydantic.error_wrappers import ValidationError

from app.interfaces.forestry_logic import IForestryLogic
from app.models.forestry_dto import ForestryDto
from app.dao_imp.forestry_dao_imp import ForestryDaoImp

class ForestryLogic(IForestryLogic):
    def save(forestry_data: dict):
        try:
            forestry_dto = ForestryDto(**forestry_data)
        except ValidationError:
            raise

        return ForestryDaoImp.save(forestry_dto)

    def getAll():
        forestries = ForestryDaoImp.getAll()
        return list(f.dict() for f in forestries)