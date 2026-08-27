import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    email = Column(String(255), unique=True, index=True, nullable=True)
    phone = Column(String(20), unique=True, index=True, nullable=False)
    full_name = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(30), default="farmer", index=True, nullable=False)  # farmer, trader, admin
    preferred_language = Column(String(20), default="hi")  # hi, en, mr
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    profile = relationship("FarmerProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    farming_records = relationship("FarmingRecord", back_populates="user", cascade="all, delete-orphan")
    conversations = relationship("ConversationSession", back_populates="user", cascade="all, delete-orphan")
    route_queries = relationship("RouteQuery", back_populates="user", cascade="all, delete-orphan")
    trader_evaluations = relationship("TraderEvaluation", back_populates="user", cascade="all, delete-orphan")
    alerts = relationship("DailyAlert", back_populates="user", cascade="all, delete-orphan")


class FarmerProfile(Base):
    __tablename__ = "farmer_profiles"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    primary_district = Column(String(100), default="Nashik", index=True)
    primary_state = Column(String(100), default="Maharashtra")
    default_crop = Column(String(100), default="Tomato")
    land_size_acres = Column(Float, default=2.0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", back_populates="profile")
