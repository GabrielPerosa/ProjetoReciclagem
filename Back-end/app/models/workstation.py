from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class WorkstationDB(Base):
    __tablename__ = "workstations"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)

    states = relationship("WorkstationStateDB", back_populates="workstation")
