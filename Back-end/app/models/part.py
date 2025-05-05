from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class PartDB(Base):
    __tablename__ = "parts"
    
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    cycle_id = Column(Integer, ForeignKey("cycles.id"), nullable=False)

    cycle = relationship("CycleDB", back_populates="parts")
