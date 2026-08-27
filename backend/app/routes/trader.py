from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.trader import (
    TraderOfferRequest,
    TraderOfferResponse,
    BargainingRequest,
    BargainingResponse,
)
from app.services.trader_service import TraderService
from app.auth.jwt import get_optional_current_user

router = APIRouter(prefix="/trader", tags=["Trader Offer & Bargaining"])


@router.post("/evaluate", response_model=TraderOfferResponse, summary="Evaluate Trader Offer")
def evaluate_trader_offer(
    payload: TraderOfferRequest,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_current_user)
):
    """
    Evaluate a middleman trader's price offer against real-time wholesale mandi benchmarks.
    Warns the farmer if the offer is below fair farm-gate value and suggests a counter-offer target.
    """
    return TraderService.evaluate_offer(db, payload, current_user)


@router.post("/bargaining-advice", response_model=BargainingResponse, summary="Get Bargaining Script")
def get_bargaining_advice(payload: BargainingRequest):
    """
    Generate tailored bargaining dialogue and actionable negotiation points
    in Hindi and English for farmers to negotiate confidently with traders.
    """
    return TraderService.get_bargaining_advice(payload)
