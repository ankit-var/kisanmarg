from datetime import date
from typing import Optional, List
from pydantic import BaseModel, Field


class MandiPriceQuery(BaseModel):
    crop: str = Field("tomato", description="Name of the crop, e.g. tomato, onion, potato")
    district: Optional[str] = Field("Nashik", description="Farmer district")
    quantity: Optional[float] = Field(500.0, description="Quantity in kg")


class MandiInfo(BaseModel):
    id: int
    name: str
    hindi_name: str
    district: str
    state: str
    distance_km: Optional[float] = None
    price_per_kg: float
    min_price_quintal: float
    max_price_quintal: float
    modal_price_quintal: float
    grade: str = "Grade A"
    price_date: date

    class Config:
        from_attributes = True


class MandiPriceResponse(BaseModel):
    crop: str
    crop_hindi: str
    district: str
    queried_at: str
    mandis_count: int
    data: List[MandiInfo]
