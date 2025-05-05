from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime

class WorkstationStateDB(Base):
    __tablename__ = "workstation_states"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    workstation_id = Column(Integer, ForeignKey("workstations.id"), nullable=False)
    
    workstation = relationship("WorkstationDB", back_populates="states")
