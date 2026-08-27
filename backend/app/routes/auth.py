from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User, FarmerProfile
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin,
    Token,
    FarmerProfileCreate,
    FarmerProfileResponse,
)
from app.auth.security import verify_password, get_password_hash
from app.auth.jwt import create_access_token, get_current_active_user

router = APIRouter(prefix="/auth", tags=["User & Authentication"])


@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED, summary="Farmer Registration")
def register_farmer(payload: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new farmer user account with mobile number, name, password, and primary district.
    """
    # Check phone duplication
    existing_phone = db.query(User).filter(User.phone == payload.phone).first()
    if existing_phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this mobile number is already registered"
        )

    # Check email duplication if provided
    if payload.email:
        existing_email = db.query(User).filter(User.email == payload.email).first()
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user with this email address is already registered"
            )

    # Create User
    new_user = User(
        phone=payload.phone,
        email=payload.email,
        full_name=payload.full_name,
        hashed_password=get_password_hash(payload.password),
        preferred_language=payload.preferred_language or "hi",
        is_active=True,
    )
    db.add(new_user)
    db.flush()

    # Create Farmer Profile
    new_profile = FarmerProfile(
        user_id=new_user.id,
        primary_district=payload.primary_district or "Nashik",
        default_crop=payload.default_crop or "Tomato",
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_user)

    # Generate JWT
    access_token = create_access_token(subject=new_user.id)
    return Token(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse.from_orm(new_user)
    )


@router.post("/login", response_model=Token, summary="Farmer Login")
def login_farmer(payload: UserLogin, db: Session = Depends(get_db)):
    """
    Authenticate farmer via phone or email + password.
    """
    user = None
    if payload.phone:
        user = db.query(User).filter(User.phone == payload.phone).first()
    elif payload.email:
        user = db.query(User).filter(User.email == payload.email).first()

    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect phone/email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user account"
        )

    access_token = create_access_token(subject=user.id)
    return Token(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse.from_orm(user)
    )


@router.get("/me", response_model=UserResponse, summary="Get Current Farmer Profile")
def get_farmer_me(current_user: User = Depends(get_current_active_user)):
    """
    Fetch the currently authenticated farmer's account details and agricultural profile.
    """
    return current_user


@router.put("/profile", response_model=FarmerProfileResponse, summary="Update Farmer Agricultural Profile")
def update_profile(
    payload: FarmerProfileCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Update default district, default crop, and land acreage.
    """
    profile = db.query(FarmerProfile).filter(FarmerProfile.user_id == current_user.id).first()
    if not profile:
        profile = FarmerProfile(user_id=current_user.id, **payload.dict())
        db.add(profile)
    else:
        for key, value in payload.dict().items():
            setattr(profile, key, value)
    
    db.commit()
    db.refresh(profile)
    return profile
