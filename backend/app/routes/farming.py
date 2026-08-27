from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.farming import FarmingRecord
from app.schemas.farming import (
    FarmingRecordCreate,
    FarmingRecordUpdate,
    FarmingRecordResponse,
)
from app.auth.jwt import get_current_active_user

router = APIRouter(prefix="/farming", tags=["Farmer Crop & Agriculture Records"])


@router.post("/records", response_model=FarmingRecordResponse, status_code=status.HTTP_201_CREATED, summary="Create Farming Record")
def create_farming_record(
    payload: FarmingRecordCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Add a new crop farming record for the authenticated farmer.
    """
    record = FarmingRecord(
        user_id=current_user.id,
        **payload.dict()
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@router.get("/records", response_model=List[FarmingRecordResponse], summary="List Farmer's Crop Records")
def get_farming_records(
    status_filter: Optional[str] = None,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Retrieve all agricultural crop records for the logged-in farmer.
    """
    query = db.query(FarmingRecord).filter(FarmingRecord.user_id == current_user.id)
    if status_filter:
        query = query.filter(FarmingRecord.status == status_filter)
    return query.order_by(FarmingRecord.created_at.desc()).all()


@router.get("/records/{record_id}", response_model=FarmingRecordResponse, summary="Get Single Farming Record")
def get_single_farming_record(
    record_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Fetch a single farming record by its ID.
    """
    record = db.query(FarmingRecord).filter(
        FarmingRecord.id == record_id,
        FarmingRecord.user_id == current_user.id
    ).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Farming record not found")
    return record


@router.put("/records/{record_id}", response_model=FarmingRecordResponse, summary="Update Farming Record")
def update_farming_record(
    record_id: str,
    payload: FarmingRecordUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Update details or status of an existing farming record.
    """
    record = db.query(FarmingRecord).filter(
        FarmingRecord.id == record_id,
        FarmingRecord.user_id == current_user.id
    ).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Farming record not found")

    for key, value in payload.dict(exclude_unset=True).items():
        setattr(record, key, value)

    db.commit()
    db.refresh(record)
    return record


@router.delete("/records/{record_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Farming Record")
def delete_farming_record(
    record_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Delete a farming record.
    """
    record = db.query(FarmingRecord).filter(
        FarmingRecord.id == record_id,
        FarmingRecord.user_id == current_user.id
    ).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Farming record not found")

    db.delete(record)
    db.commit()
    return None
