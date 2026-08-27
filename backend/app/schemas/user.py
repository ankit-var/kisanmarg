from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class FarmerProfileBase(BaseModel):
    primary_district: str = "Nashik"
    primary_state: str = "Maharashtra"
    default_crop: str = "Tomato"
    land_size_acres: float = 2.0


class FarmerProfileCreate(FarmerProfileBase):
    pass


class FarmerProfileResponse(FarmerProfileBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    phone: str = Field(..., description="Indian 10-digit mobile number, e.g., 9876543210")
    full_name: str = Field(..., min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    role: str = Field("farmer", description="User role: farmer, trader, admin")
    preferred_language: str = "hi"


class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=100)
    primary_district: Optional[str] = "Nashik"
    default_crop: Optional[str] = "Tomato"


class UserLogin(BaseModel):
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    password: str


class UserResponse(UserBase):
    id: str
    is_active: bool
    created_at: datetime
    profile: Optional[FarmerProfileResponse] = None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class TokenPayload(BaseModel):
    sub: Optional[str] = None
    exp: Optional[int] = None
