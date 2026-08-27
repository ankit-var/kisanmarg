from fastapi import APIRouter
from app.schemas.voice import VoiceIntentRequest, VoiceIntentResponse
from app.services.voice_ai_service import VoiceAIService

router = APIRouter(prefix="/voice", tags=["Voice Assistant AI"])


@router.post("/process-intent", response_model=VoiceIntentResponse, summary="Process Spoken Voice Intent")
def process_voice_intent(payload: VoiceIntentRequest):
    """
    Process speech transcripts in Hindi/Hinglish to extract farmer intent,
    relevant entities (crop, district, price, quantity), and recommend the next screen.
    """
    return VoiceAIService.process_intent(payload)
