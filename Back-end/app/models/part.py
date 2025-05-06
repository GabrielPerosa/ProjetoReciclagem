from sqlalchemy import Column, String, ForeignKey, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class PartDB(Base):
    __tablename__ = "parts"
    
    id = Column(String, primary_key=True, index=True)
    type = Column(String, nullable=False)
    cycle_id = Column(String, ForeignKey("cycles.id"), nullable=False)

    cycle = relationship("CycleDB", back_populates="parts")
