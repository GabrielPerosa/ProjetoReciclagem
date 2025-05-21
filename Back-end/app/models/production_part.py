from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
import uuid

class ProductionPartDB(Base):
    __tablename__ = "production_parts"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    part_id = Column(String, ForeignKey("parts.id"), nullable=False)
    stored_quantity = Column(Integer, nullable=False)
    cycle_id = Column(String, ForeignKey("cycle.id"), nullable=False)

    part = relationship("PartDB", back_populates="productions")
    cycle = relationship("CycleDB")

from app.models.cycle import CycleDB
from app.models.part import PartDB
