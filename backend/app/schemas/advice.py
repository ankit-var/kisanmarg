from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class AdviceRequest(BaseModel):
    district: str = Field("Nashik", description="Farmer's origin district")
    quantity: Any = Field("500 Kg", description="Harvest quantity, e.g. 500 or '500 Kg'")
    crop: str = Field("tomato", description="Crop name, e.g. tomato")
    language: Optional[str] = Field("hi", description="Preferred response language ('hi' or 'en')")


class MandiComparisonItem(BaseModel):
    mandi_name: str
    mandi_hindi: str
    district: str
    gross_price_per_kg: float
    distance_km: float
    transport_cost_total: float
    transport_cost_per_kg: float
    net_price_per_kg: float
    total_net_payout: float
    is_recommended: bool = False


class AdviceResponse(BaseModel):
    success: bool = True
    crop: str
    crop_hindi: str
    district: str
    quantity_kg: float
    
    # Primary Advice Card Data
    recommended_mandi: str
    recommended_mandi_hi: str
    mandi_price_per_kg: float
    transport_cost_per_kg: float
    net_price_per_kg: float
    
    # Fact Cards Data
    extra_gain_per_kg: float
    total_extra_gain: float
    distance_km: float
    
    # Spoken Audio Script
    spoken_text: str
    spoken_text_hi: str
    spoken_text_en: str
    audio_duration_seconds: float = 14.0
    
    # Comparative Breakdown
    comparisons: List[MandiComparisonItem]
