import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class TraderEvaluation(Base):
    __tablename__ = "trader_evaluations"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    crop = Column(String(100), nullable=False, default="tomato")
    district = Column(String(100), nullable=False, default="Nashik")
    offer_price_per_kg = Column(Float, nullable=False)
    
    benchmark_mandi_price = Column(Float, nullable=False)
    target_price_per_kg = Column(Float, nullable=False)
    target_price_max = Column(Float, nullable=False)
    
    is_fair_price = Column(Boolean, default=False)
    verdict = Column(String(50), default="कम भाव")  # कम भाव, उचित भाव, उत्कृष्ट भाव
    
    warning_text_hi = Column(Text, nullable=False)
    warning_text_en = Column(Text, nullable=False)
    bargaining_script_hi = Column(Text, nullable=False)
    bargaining_script_en = Column(Text, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow, index=True)

    # Relationships
    user = relationship("User", back_populates="trader_evaluations")
