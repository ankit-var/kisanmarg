from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class FarmingRecordBase(BaseModel):
    crop_name: str = Field(..., description="Crop name, e.g. Tomato, Onion")
    variety: Optional[str] = Field("Hybrid", description="Seed variety")
    area_acres: float = Field(1.5, ge=0.1, description="Planted area in acres")
    sowing_date: Optional[date] = Field(default_factory=date.today)
    harvest_expected_date: Optional[date] = None
    estimated_yield_kg: float = Field(5000.0, ge=0, description="Estimated total harvest yield in kg")
    status: str = Field("growing", description="Status: sown, growing, ready_for_harvest, harvested")
    notes: Optional[str] = None


class FarmingRecordCreate(FarmingRecordBase):
    pass


class FarmingRecordUpdate(BaseModel):
    crop_name: Optional[str] = None
    variety: Optional[str] = None
    area_acres: Optional[float] = None
    sowing_date: Optional[date] = None
    harvest_expected_date: Optional[date] = None
    estimated_yield_kg: Optional[float] = None
    status: Optional[str] = None
    notes: Optional[str] = None


class FarmingRecordResponse(FarmingRecordBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
