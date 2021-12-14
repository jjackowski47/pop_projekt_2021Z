from abc import ABCMeta
from pydantic.types import UUID4

from app.database import Database

with Database() as db:
    class AuthenticationDaoImp(metaclass=ABCMeta):
        def generateToken(token: UUID4):
            token_row = db.TokenRow(value=token)
            db.session.add(token_row)
            db.session.commit()
            return token_row.value

        def tokenExists(token: str):
            return db.session.query(db.TokenRow.id).filter_by(value=token).first() is not None
