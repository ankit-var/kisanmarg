from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.mandi import Mandi, Commodity
from app.schemas.mandi import MandiPriceQuery, MandiPriceResponse
from app.services.mandi_service import MandiService

router = APIRouter(prefix="/mandi", tags=["Mandi Market Prices"])


@router.post("/prices", response_model=MandiPriceResponse, summary="Query Mandi Prices")
def get_mandi_prices(payload: MandiPriceQuery, db: Session = Depends(get_db)):
    """
    Get live/modal wholesale mandi prices for a given crop and district.
    Used by the frontend to compare regional mandi rates.
    """
    return MandiService.get_prices(db, payload)


@router.get("/list", summary="List All Active Mandis")
def list_mandis(district: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Get a list of all registered APMC mandis, optionally filtered by district.
    """
    query = db.query(Mandi).filter(Mandi.is_active == True)
    if district:
        query = query.filter(Mandi.district.ilike(f"%{district}%"))
    mandis = query.all()
    return [
        {
            "id": m.id,
            "name": m.name,
            "hindi_name": m.hindi_name,
            "district": m.district,
            "state": m.state,
            "latitude": m.latitude,
            "longitude": m.longitude,
        }
        for m in mandis
    ]


@router.get("/commodities", summary="List Supported Agricultural Commodities")
def list_commodities(db: Session = Depends(get_db)):
    """
    List all supported crops (e.g., Tomato, Onion, Potato, Wheat, Soybean).
    """
    commodities = db.query(Commodity).all()
    return [
        {
            "id": c.id,
            "name": c.name,
            "hindi_name": c.hindi_name,
            "category": c.category,
            "unit": c.unit,
        }
        for c in commodities
    ]
