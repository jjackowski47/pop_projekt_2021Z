from pydantic.types import UUID1
from app.database import Database
from app.interfaces.forestry_dao import ForestryDao
from app.models.forestry_dto import ForestryDto


class Forestry(ForestryDao):
    def save(forestryDto: ForestryDto):
        with Database() as db:
            return db.execute(f"INSERT INTO forestry(location, name) VALUES ('{','.join([f'({coord.x}, {coord.y})' for coord in forestryDto.location])}', '{forestryDto.name}');")

    def getAll():
        with Database() as db:
            return db.query('SELECT * FROM forestry')

    def existsById(id: UUID1) -> bool:
        with Database() as db:
            result = db.query(
                f"SELECT 1 WHERE EXISTS (SELECT * FROM forestry WHERE id='{id}');")
            return True if result else False
