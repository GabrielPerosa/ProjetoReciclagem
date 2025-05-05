from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime

class CycleDB(Base):
    __tablename__ = "cycles"

    id = Column(Integer, primary_key=True, index=True)
    initial_time = Column(DateTime(default=datetime.utcnow))
    end_time = Column(DateTime(default=datetime.utcnow))

    parts = relationship("PartDB", back_populates="cycle")
