from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class CycleDB(Base):
    __tablename__ = "cycles"

    id = Column(Integer, primary_key=True, index=True)
    initial_time = Column(DateTime)
    end_time = Column(DateTime)
    part_id = Column(Integer, ForeignKey("parts.id"), nullable=False)

    part = relationship("PartDB", back_populates="cycles")
