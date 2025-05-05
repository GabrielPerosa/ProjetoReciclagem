from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class SensorDB(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)

    states = relationship("SensorStateDB", back_populates="sensor")
