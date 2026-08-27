from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Commodity(Base):
    __tablename__ = "commodities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)  # e.g., Tomato
    hindi_name = Column(String(100), nullable=False)                     # e.g., टमाटर
    category = Column(String(50), default="Vegetables")                  # Vegetables, Fruits, Grains
    unit = Column(String(20), default="kg")
    image_url = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    prices = relationship("MandiPrice", back_populates="commodity", cascade="all, delete-orphan")


class Mandi(Base):
    __tablename__ = "mandis"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, index=True, nullable=False)  # e.g., Lasalgaon Mandi
    hindi_name = Column(String(150), nullable=False)                     # e.g., लासलगाँव मंडी
    district = Column(String(100), index=True, nullable=False)          # e.g., Nashik
    state = Column(String(100), default="Maharashtra")
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    prices = relationship("MandiPrice", back_populates="mandi", cascade="all, delete-orphan")


class MandiPrice(Base):
    __tablename__ = "mandi_prices"

    id = Column(Integer, primary_key=True, index=True)
    mandi_id = Column(Integer, ForeignKey("mandis.id", ondelete="CASCADE"), nullable=False, index=True)
    commodity_id = Column(Integer, ForeignKey("commodities.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Prices in ₹ per Quintal (100 kg) and ₹ per Kg
    min_price_quintal = Column(Float, nullable=False)
    max_price_quintal = Column(Float, nullable=False)
    modal_price_quintal = Column(Float, nullable=False)
    price_per_kg = Column(Float, nullable=False, index=True)  # Derived modal_price / 100
    
    arrivals_tonnes = Column(Float, default=150.0)
    grade = Column(String(20), default="Grade A")
    price_date = Column(Date, default=date.today, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    mandi = relationship("Mandi", back_populates="prices")
    commodity = relationship("Commodity", back_populates="prices")
