from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.conversation import ConversationSession, ChatMessage
from app.schemas.conversation import (
    ConversationSessionCreate,
    ConversationSessionResponse,
    ChatMessageCreate,
    ChatMessageResponse,
)
from app.auth.jwt import get_current_active_user, get_optional_current_user

router = APIRouter(prefix="/conversation", tags=["AI Conversation & Chat History"])


@router.post("/sessions", response_model=ConversationSessionResponse, status_code=status.HTTP_201_CREATED, summary="Start Conversation Session")
def create_session(
    payload: ConversationSessionCreate,
    current_user: Optional[User] = Depends(get_optional_current_user),
    db: Session = Depends(get_db)
):
    """
    Start a new voice/chat conversation session.
    """
    session = ConversationSession(
        user_id=current_user.id if current_user else None,
        session_title=payload.session_title or "मंडी भाव बातचीत (Mandi Query)",
        language=payload.language or "hi"
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


@router.get("/sessions", response_model=List[ConversationSessionResponse], summary="List Farmer's Conversation Sessions")
def get_user_sessions(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get all past conversation sessions for the authenticated farmer.
    """
    return db.query(ConversationSession).filter(
        ConversationSession.user_id == current_user.id
    ).order_by(ConversationSession.created_at.desc()).all()


@router.post("/sessions/{session_id}/messages", response_model=ChatMessageResponse, status_code=status.HTTP_201_CREATED, summary="Add Message to Session")
def add_chat_message(
    session_id: str,
    payload: ChatMessageCreate,
    current_user: Optional[User] = Depends(get_optional_current_user),
    db: Session = Depends(get_db)
):
    """
    Append a user query or assistant response into an active conversation session.
    """
    session = db.query(ConversationSession).filter(ConversationSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation session not found")

    message = ChatMessage(
        session_id=session_id,
        user_id=current_user.id if current_user else None,
        **payload.dict()
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


@router.get("/sessions/{session_id}", response_model=ConversationSessionResponse, summary="Get Full Conversation Session with Messages")
def get_session_details(
    session_id: str,
    db: Session = Depends(get_db)
):
    """
    Retrieve conversation session details and full history of chat messages.
    """
    session = db.query(ConversationSession).filter(ConversationSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation session not found")
    return session
