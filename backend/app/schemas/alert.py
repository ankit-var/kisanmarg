from typing import Optional
from pydantic import BaseModel, Field


class AlertSubscribeRequest(BaseModel):
    crop: str = Field("tomato", description="Crop name for alerts")
    district: str = Field("Nashik", description="District for mandi prices")
    enabled: bool = Field(True, description="Enable or disable daily alert")
    phone: Optional[str] = Field(None, description="Farmer's WhatsApp or SMS number")
    channel: Optional[str] = Field("whatsapp_and_audio", description="Channel: whatsapp_and_audio, sms, voice_call")


class AlertResponse(BaseModel):
    success: bool = True
    message: str
    message_hi: str
    crop: str
    district: str
    enabled: bool
    scheduled_time: str = "08:00 AM"
    delivery_channel: str = "WhatsApp & Audio Message"
