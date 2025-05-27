from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class PartDB(Base):
    __tablename__ = "parts"
    
    id = Column(String, primary_key=True, index=True)
    type = Column(String, nullable=False)
    
    productions = relationship("ProductionPartDB", back_populates="part", foreign_keys="ProductionPartDB.part_id")
