import re
from typing import Dict, Any
from app.schemas.voice import VoiceIntentRequest, VoiceIntentResponse


class VoiceAIService:
    @staticmethod
    def process_intent(request: VoiceIntentRequest) -> VoiceIntentResponse:
        transcript = request.transcript.strip()
        text_lower = transcript.lower()

        extracted_entities: Dict[str, Any] = {}
        intent = "GENERAL_HELP"
        next_route = "/district"
        spoken_reply_hi = "कृपया अपनी फसल और जिले का नाम बताएं।"
        spoken_reply_en = "Please tell me your crop name and district."

        # 1. Extract Crop
        if any(w in text_lower for w in ["टमाटर", "tomato", "tamatar"]):
            extracted_entities["crop"] = "tomato"
            extracted_entities["crop_hindi"] = "टमाटर"
        elif any(w in text_lower for w in ["प्याज", "कांदा", "onion", "pyaz"]):
            extracted_entities["crop"] = "onion"
            extracted_entities["crop_hindi"] = "प्याज"
        elif any(w in text_lower for w in ["आलू", "potato", "aalu"]):
            extracted_entities["crop"] = "potato"
            extracted_entities["crop_hindi"] = "आलू"
        elif any(w in text_lower for w in ["गेहूँ", "wheat", "gehu"]):
            extracted_entities["crop"] = "wheat"
            extracted_entities["crop_hindi"] = "गेहूँ"

        # 2. Extract District
        if "nashik" in text_lower or "नासिक" in text_lower or "नाशिक" in text_lower:
            extracted_entities["district"] = "Nashik"
        elif "pune" in text_lower or "पुणे" in text_lower:
            extracted_entities["district"] = "Pune"
        elif "ahmednagar" in text_lower or "अहमदनगर" in text_lower or "नगर" in text_lower:
            extracted_entities["district"] = "Ahmednagar"
        elif "solapur" in text_lower or "सोलापुर" in text_lower:
            extracted_entities["district"] = "Solapur"

        # 3. Extract Numerical Figures (Prices or Quantities)
        numbers = re.findall(r'\d+', text_lower)
        if numbers:
            if "किलो" in text_lower or "kg" in text_lower or "क्विंटल" in text_lower:
                extracted_entities["quantity"] = float(numbers[0])
            elif "रुपये" in text_lower or "₹" in text_lower or "भाव" in text_lower or "बताया" in text_lower:
                extracted_entities["offerPrice"] = float(numbers[0])

        # 4. Intent Classification
        if any(w in text_lower for w in ["व्यापारी", "trader", "दलाल", "दिया", "बताया", "offer"]):
            intent = "TRADER_OFFER"
            next_route = "/trader-offer"
            spoken_reply_hi = "व्यापारी का भाव जाँचने के लिए चलिए।"
            spoken_reply_en = "Let's check the trader's offer against regional mandi prices."
        elif any(w in text_lower for w in ["कहाँ बेचूँ", "कहा बेचू", "कहाँ ले जाऊं", "best mandi", "मंडी"]):
            intent = "BEST_MANDI"
            next_route = "/district"
            spoken_reply_hi = "आइए पता करें कि आपके लिए सबसे अच्छी मंडी कौन सी है।"
            spoken_reply_en = "Let's find the most profitable APMC mandi for your harvest."
        elif any(w in text_lower for w in ["भाव बढ़ेगा", "trend", "कल का भाव", "तेजी"]):
            intent = "PRICE_TREND"
            next_route = "/advice"
            spoken_reply_hi = "बाज़ार में मांग और आने वाले दिनों के भाव का रुझान देखते हैं।"
            spoken_reply_en = "Let's analyze market demand and upcoming price trends."
        elif any(w in text_lower for w in ["भाव", "price", "रेट", "rate", "टमाटर का"]):
            intent = "PRICE_QUERY"
            next_route = "/district"
            spoken_reply_hi = "आज के ताज़ा मंडी भाव जानने के लिए अपना जिला चुनें।"
            spoken_reply_en = "Select your district to see today's latest mandi rates."
        elif any(w in text_lower for w in ["अलर्ट", "alert", "रोज़", "daily"]):
            intent = "ALERT_SETUP"
            next_route = "/daily-alert"
            spoken_reply_hi = "रोज़ाना भाव का अलर्ट सेट करने के लिए यहाँ आएँ।"
            spoken_reply_en = "Let's set up your daily price notification alert."

        return VoiceIntentResponse(
            success=True,
            transcript=transcript,
            intent=intent,
            extracted_entities=extracted_entities,
            next_route=next_route,
            spoken_reply_hi=spoken_reply_hi,
            spoken_reply_en=spoken_reply_en,
            confidence=0.95
        )
