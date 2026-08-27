from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field


class VoiceIntentRequest(BaseModel):
    transcript: str = Field(..., description="Spoken Hindi/Hinglish text transcript, e.g. 'टमाटर कहाँ बेचूँ?'")
    language: Optional[str] = Field("hi", description="Language code ('hi', 'en', 'mr')")


class VoiceIntentResponse(BaseModel):
    success: bool = True
    transcript: str
    intent: str                   # 'PRICE_QUERY', 'TRADER_OFFER', 'BEST_MANDI', 'PRICE_TREND', 'ALERT_SETUP', 'GENERAL_HELP'
    extracted_entities: Dict[str, Any]  # {'crop': 'tomato', 'district': 'Nashik', 'price': 20, 'quantity': 500}
    next_route: str               # e.g., '/district', '/trader-offer', '/advice'
    spoken_reply_hi: str
    spoken_reply_en: str
    confidence: float = 0.95
