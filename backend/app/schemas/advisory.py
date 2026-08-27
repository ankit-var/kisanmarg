from typing import List, Optional
from pydantic import BaseModel


class WeatherForecastItem(BaseModel):
    date: str
    condition: str
    condition_hi: str
    temp_max: float
    temp_min: float
    rainfall_prob_percent: int
    humidity_percent: int
    impact_on_harvest: str
    impact_on_harvest_hi: str


class WeatherAdvisoryResponse(BaseModel):
    district: str
    state: str
    current_temp_celsius: float
    condition: str
    condition_hi: str
    harvest_recommendation: str
    harvest_recommendation_hi: str
    forecast: List[WeatherForecastItem]


class CropTipItem(BaseModel):
    topic: str
    topic_hi: str
    advice: str
    advice_hi: str
    severity: str = "normal"  # normal, warning, tip


class CropAdvisoryResponse(BaseModel):
    crop: str
    crop_hindi: str
    district: str
    season: str
    market_trend: str
    market_trend_hi: str
    storage_advice: str
    storage_advice_hi: str
    tips: List[CropTipItem]
