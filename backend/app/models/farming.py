import uuid
from datetime import datetime, date
from sqlalchemy import Column, String, Float, DateTime, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class FarmingRecord(Base):
    __tablename__ = "farming_records"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    crop_name = Column(String(100), nullable=False, index=True)  # e.g., Tomato
    variety = Column(String(100), default="Abhinav / Hybrid")
    area_acres = Column(Float, default=1.5)
    sowing_date = Column(Date, default=date.today)
    harvest_expected_date = Column(Date, nullable=True)
    estimated_yield_kg = Column(Float, default=5000.0)
    
    status = Column(String(50), default="growing", index=True)  # sown, growing, ready_for_harvest, harvested
    notes = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", back_populates="farming_records")
