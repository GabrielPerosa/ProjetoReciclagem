from sqlalchemy import Column, Integer, String
from app.config.database import Base

class SensorDB(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)