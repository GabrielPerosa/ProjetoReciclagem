from sqlalchemy import Column, Integer, String
from app.config.database import Base

class WorkstationState(Base):
    __tablename__ = "workstation_states"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)
