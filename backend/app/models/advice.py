import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from app.database import Base


class RouteQuery(Base):
    __tablename__ = "route_queries"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    crop = Column(String(100), nullable=False, default="tomato")
    district = Column(String(100), nullable=False, default="Nashik")
    quantity_kg = Column(Float, nullable=False, default=500.0)
    user_language = Column(String(20), default="hi")
    created_at = Column(DateTime, default=datetime.utcnow, index=True)

    # Relationships
    user = relationship("User", back_populates="route_queries")
    advice_result = relationship("AdviceResult", back_populates="query", uselist=False, cascade="all, delete-orphan")


class AdviceResult(Base):
    __tablename__ = "advice_results"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    query_id = Column(String(36), ForeignKey("route_queries.id", ondelete="CASCADE"), nullable=False, unique=True)
    
    recommended_mandi = Column(String(150), nullable=False)
    recommended_mandi_hi = Column(String(150), nullable=False)
    mandi_price_per_kg = Column(Float, nullable=False)
    transport_cost_per_kg = Column(Float, nullable=False)
    net_price_per_kg = Column(Float, nullable=False)
    
    nearby_mandi = Column(String(150), nullable=False)
    nearby_mandi_hi = Column(String(150), nullable=False)
    nearby_price_per_kg = Column(Float, nullable=False)
    
    extra_gain_per_kg = Column(Float, nullable=False)
    total_extra_gain = Column(Float, nullable=False)
    distance_km = Column(Float, nullable=False)
    
    spoken_text_hi = Column(Text, nullable=False)
    spoken_text_en = Column(Text, nullable=False)
    audio_duration_seconds = Column(Float, default=14.0)
    
    breakdown = Column(JSON, nullable=True)  # Detailed list of all compared mandis
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    query = relationship("RouteQuery", back_populates="advice_result")
