from datetime import datetime
from sqlalchemy.orm import session
from sqlalchemy.sql.elements import Null

from app.database import Database
from app.interfaces.sensor_reading_dao import SensorReadingDao
from app.models.sensor_dto import SensorReadingDto

with Database() as db:

    class SensorReadingImp(SensorReadingDao):
        def registerReading(sensor_reading_dto: SensorReadingDto):
            sensor_reading_row = db.SensorReadingRow(
                reading=sensor_reading_dto.reading, readtime=datetime.utcnow, sensor_id=sensor_reading_dto.sensorId
            )
            db.session.add(sensor_reading_row)
            db.session.commit()
