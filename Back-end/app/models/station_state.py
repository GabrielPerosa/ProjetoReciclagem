from sqlalchemy import Column, Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class StationStateDB(Base):
    __tablename__ = "station_states"

    id = Column(String, primary_key=True, index=True)
    station_id = Column(String, ForeignKey("stations.id"), nullable=False)
    cycle_id = Column(String, nullable=False)
    state = Column(Boolean, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    station = relationship("StationDB", back_populates="states")