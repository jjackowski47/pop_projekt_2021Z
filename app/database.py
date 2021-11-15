from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

import os

DB_URL = 'postgresql+psycopg2://' + os.getenv('DATABASE_URL')


class Database:
    def __init__(self):
        self.Base = automap_base()
        self.engine = create_engine(DB_URL)
        self.Base.prepare(self.engine, reflect=True)
        self.ForestryRow = self.Base.classes.forestry
        self.SensorRow = self.Base.classes.sensor

    def __enter__(self):
        self.session = Session(self.engine)
        return self

    def __exit__(self, exc_type, exc_value, tb):
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            self.session.flush()
            raise e
        finally:
            self.session.close()
        return True
