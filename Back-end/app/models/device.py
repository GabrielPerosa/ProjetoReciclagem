from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class DeviceDB(Base):
    __tablename__ = "devices"

    id = Column(String, primary_key=True, index=True)
    description = Column(String, nullable=False)

    states = relationship("DeviceStateDB", back_populates="device", cascade="all, delete-orphan")
