from sqlalchemy import Column, Integer, String
from app.config.database import Base

class Workstation(Base):
    __tablename__ = "workstations"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
