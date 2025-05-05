from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime

class SensorStateDB(Base):
    __tablename__ = "sensor_states"

    id = Column(Integer, primary_key=True, index=True)
    state = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    sensor_id = Column(Integer, ForeignKey("sensors.id"), nullable=False)

    sensor = relationship("SensorDB", back_populates="states")