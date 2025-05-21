from sqlalchemy import Column, Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class StationStateDB(Base):
    __tablename__ = "station_states"
    id: int = Column(String, primary_key=True)
    station_id = Column(String, ForeignKey("stations.id"), primary_key=True)
    cycle_id = Column(String, ForeignKey("cycle.id"), primary_key=True)
    timestamp = Column(DateTime, primary_key=True) 
    state = Column(Boolean, nullable=False)

    station = relationship("StationDB", back_populates="states")
    cycle = relationship("CycleDB", back_populates="station_states")
