from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class PartDB(Base):
    __tablename__ = "parts"
    
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)

    cycles = relationship("CycleDB", back_populates="part")
