import uuid
from datetime import datetime, time
from sqlalchemy import Column, String, Boolean, DateTime, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class DailyAlert(Base):
    __tablename__ = "daily_alerts"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=True, index=True)
    phone = Column(String(20), nullable=True, index=True)
    crop = Column(String(100), default="tomato", index=True)
    district = Column(String(100), default="Nashik", index=True)
    channel = Column(String(30), default="whatsapp_and_audio")  # whatsapp, sms, voice_call, push
    scheduled_time = Column(Time, default=time(8, 0))  # 08:00 AM
    is_active = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="alerts")


class NotificationLog(Base):
    __tablename__ = "notification_logs"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    alert_id = Column(String(36), ForeignKey("daily_alerts.id", ondelete="CASCADE"), nullable=False, index=True)
    recipient = Column(String(50), nullable=False)
    status = Column(String(30), default="sent")  # sent, delivered, failed
    message_content = Column(String(500), nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
