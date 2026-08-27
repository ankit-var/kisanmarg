from typing import Optional, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.advice import RouteQuery, AdviceResult
from app.schemas.advice import AdviceRequest, AdviceResponse
from app.services.advice_service import AdviceService
from app.auth.jwt import get_optional_current_user, get_current_active_user

router = APIRouter(prefix="/advice", tags=["AI Market Advice"])


@router.post("/recommend", response_model=AdviceResponse, summary="Get AI Route & Market Advice")
def get_market_advice(
    payload: AdviceRequest,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_current_user)
):
    """
    Generate the optimal APMC mandi recommendation by combining wholesale prices,
    freight logistics calculations, distance, and net take-home profit.
    Returns spoken audio scripts in Hindi and English.
    """
    return AdviceService.generate_recommendation(db, payload, current_user)


@router.get("/history", summary="Farmer Route Advice History")
def get_advice_history(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Retrieve past AI market recommendations requested by the logged-in farmer.
    """
    queries = db.query(RouteQuery).filter(
        RouteQuery.user_id == current_user.id
    ).order_by(RouteQuery.created_at.desc()).limit(20).all()

    results = []
    for q in queries:
        adv = q.advice_result
        if adv:
            results.append({
                "id": q.id,
                "created_at": q.created_at,
                "crop": q.crop,
                "district": q.district,
                "quantity_kg": q.quantity_kg,
                "recommended_mandi": adv.recommended_mandi_hi,
                "net_price_per_kg": adv.net_price_per_kg,
                "extra_gain_per_kg": adv.extra_gain_per_kg,
                "distance_km": adv.distance_km,
                "spoken_text": adv.spoken_text_hi
            })
    return results
