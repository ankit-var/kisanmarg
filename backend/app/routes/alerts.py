from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.alert import DailyAlert
from app.schemas.alert import AlertSubscribeRequest, AlertResponse
from app.services.alert_service import AlertService
from app.auth.jwt import get_optional_current_user, get_current_active_user

router = APIRouter(prefix="/alerts", tags=["Daily Price Alerts"])


@router.post("/subscribe", response_model=AlertResponse, summary="Subscribe to Daily Mandi Alert")
def subscribe_daily_alert(
    payload: AlertSubscribeRequest,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_current_user)
):
    """
    Subscribe or unsubscribe to daily 8:00 AM WhatsApp & Audio market price updates.
    """
    return AlertService.subscribe_alert(db, payload, current_user)


@router.get("/my-alerts", summary="List Farmer's Active Alerts")
def get_user_alerts(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Fetch all active price alerts for the authenticated farmer.
    """
    alerts = db.query(DailyAlert).filter(
        DailyAlert.user_id == current_user.id
    ).all()
    return alerts
