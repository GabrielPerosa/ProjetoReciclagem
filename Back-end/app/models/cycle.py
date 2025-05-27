from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class CycleDB(Base):
    __tablename__ = "cycle"
    
    id = Column(String, primary_key=True, index=True)
    
    station_states = relationship("StationStateDB", back_populates="cycle")
    production_parts = relationship("ProductionPartDB", back_populates="cycle")
