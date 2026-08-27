from typing import Optional
from pydantic import BaseModel, Field


class TraderOfferRequest(BaseModel):
    crop: str = Field("tomato", description="Crop name")
    offerPrice: float = Field(..., description="Trader's offer in ₹/kg (e.g., 14)")
    district: Optional[str] = Field("Nashik", description="Farmer's district")
    language: Optional[str] = Field("hi", description="Language: 'hi' or 'en'")


class TraderOfferResponse(BaseModel):
    success: bool = True
    crop: str
    crop_hindi: str
    offer_price: float
    district: str
    
    benchmark_mandi_price: float
    target_price: float
    target_price_max: float
    
    is_fair_price: bool
    verdict: str                  # e.g., "कम भाव"
    verdict_en: str               # e.g., "Low Offer"
    
    warning_text: str             # e.g., "₹14 प्रति किलो कम है. व्यापारी से कम-से-कम ₹16 माँगिए."
    warning_text_en: str
    
    bargaining_script_preview: str


class BargainingRequest(BaseModel):
    crop: str = Field("tomato", description="Crop name")
    offerPrice: float = Field(14.0, description="Trader's initial offer in ₹/kg")
    targetPrice: Optional[float] = Field(16.0, description="Target counter-offer price")
    language: Optional[str] = Field("hi", description="Language: 'hi' or 'en'")


class BargainingResponse(BaseModel):
    success: bool = True
    crop: str
    offer_price: float
    target_price: float
    target_price_max: float
    
    # Audio Speech Script
    script: str                   # "पास की मंडी में भाव अधिक है। मुझे कम-से-कम ₹16 से ₹18 प्रति किलो मिलना चाहिए।"
    script_en: str
    audio_duration: float = 12.0
    
    negotiation_tips: list[str] = []
