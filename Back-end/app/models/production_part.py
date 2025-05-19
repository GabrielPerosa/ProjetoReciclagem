from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class ProductionPartDB(Base):
    __tablename__ = "production_parts"
    
    id = Column(String, primary_key=True, index=True)
    stored_part_id = Column(String, ForeignKey("parts.id"), nullable=False)
    cycle_id = Column(String, nullable=False)

    part = relationship("PartyDB", back_populates="productions")