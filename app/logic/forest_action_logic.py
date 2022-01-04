from pydantic.error_wrappers import ValidationError
from app.interfaces.forest_action_logic import IForestActionLogic
from app.models.forest_action_dto import ForestActionDto
from app.dao_imp.forest_action_dao_imp import ForestActionDaoImp


class ForestActionLogic(IForestActionLogic):
    def save(forest_action_data: dict):
        try:
            forest_action_dto = ForestActionDto(**forest_action_data)
        except ValidationError:
            raise

        return ForestActionDaoImp.save(forest_action_dto)

    def getAll():
        forest_actions = ForestActionDaoImp.getAll()
        return list(f.dict() for f in forest_actions)
