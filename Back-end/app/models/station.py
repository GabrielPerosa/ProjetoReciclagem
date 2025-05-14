from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class StationDB(Base):
    __tablename__ = "stations"
    id = Column(String, primary_key=True, index=True)
    description = Column(String, nullable=False)
    
    states = relationship("StationStateDB", back_populates="station")