from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class ChatMessageCreate(BaseModel):
    query_transcript: str = Field(..., description="Spoken transcript or typed query")
    sender_type: str = Field("user", description="user or assistant")
    intent: Optional[str] = None
    extracted_entities: Optional[Dict[str, Any]] = None
    response_text: Optional[str] = None
    audio_script: Optional[str] = None
    audio_duration_seconds: Optional[float] = 0.0


class ChatMessageResponse(BaseModel):
    id: str
    session_id: str
    user_id: Optional[str] = None
    sender_type: str
    query_transcript: str
    intent: Optional[str] = None
    extracted_entities: Optional[Dict[str, Any]] = None
    response_text: Optional[str] = None
    audio_script: Optional[str] = None
    audio_duration_seconds: float
    created_at: datetime

    class Config:
        from_attributes = True


class ConversationSessionCreate(BaseModel):
    session_title: Optional[str] = "मंडी भाव बातचीत (Mandi Query)"
    language: Optional[str] = "hi"


class ConversationSessionResponse(BaseModel):
    id: str
    user_id: Optional[str] = None
    session_title: str
    language: str
    created_at: datetime
    updated_at: datetime
    messages: List[ChatMessageResponse] = []

    class Config:
        from_attributes = True
