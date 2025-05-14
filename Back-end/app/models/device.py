from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class DeviceStateDB(Base):
    __tablename__ = "device_states"
    id = Column(String, primary_key=True, index=True)
    device_id = Column(String, ForeignKey("devices.id"), nullable=False)
    state = Column(Boolean, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    device = relationship("DeviceDB", back_populates="states")