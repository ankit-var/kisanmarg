from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db

router = APIRouter(tags=["Health"])


@router.get("/health", summary="Health Check API")
def health_check(db: Session = Depends(get_db)):
    """
    Check the operational status of the Kisaan Marg backend server and database.
    """
    db_status = "healthy"
    try:
        db.execute(text("SELECT 1"))
    except Exception as e:
        db_status = f"unhealthy ({str(e)})"

    return {
        "status": "online",
        "service": "Kisaan Marg AI Backend",
        "version": "1.0.0",
        "database": db_status
    }
