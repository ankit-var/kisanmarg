from typing import Optional
from sqlalchemy.orm import Session
from app.models.alert import DailyAlert, NotificationLog
from app.models.user import User
from app.schemas.alert import AlertSubscribeRequest, AlertResponse


class AlertService:
    @staticmethod
    def subscribe_alert(
        db: Session,
        request: AlertSubscribeRequest,
        current_user: Optional[User] = None
    ) -> AlertResponse:
        crop_clean = request.crop.strip().lower()
        district_clean = request.district.strip()
        phone_clean = request.phone or (current_user.phone if current_user else None)

        if request.enabled:
            # Check existing subscription
            existing = db.query(DailyAlert).filter(
                DailyAlert.crop.ilike(crop_clean),
                DailyAlert.district.ilike(district_clean),
                (DailyAlert.user_id == (current_user.id if current_user else None)) | (DailyAlert.phone == phone_clean)
            ).first()

            if not existing:
                alert = DailyAlert(
                    user_id=current_user.id if current_user else None,
                    phone=phone_clean or "9876543210",
                    crop=crop_clean,
                    district=district_clean,
                    channel=request.channel or "whatsapp_and_audio",
                    is_active=True
                )
                db.add(alert)
                db.commit()
            else:
                existing.is_active = True
                db.commit()

            msg_hi = f"डेमो अलर्ट तैयार है! सुबह 8:00 बजे आपको व्हाट्सएप और ऑडियो संदेश द्वारा {district_clean} में {crop_clean} के भाव भेजे जाएंगे।"
            msg_en = f"Daily alert activated! You will receive 8:00 AM WhatsApp and audio updates for {crop_clean} in {district_clean}."
        else:
            # Disable existing alerts
            if current_user or phone_clean:
                db.query(DailyAlert).filter(
                    DailyAlert.crop.ilike(crop_clean),
                    DailyAlert.district.ilike(district_clean),
                    (DailyAlert.user_id == (current_user.id if current_user else None)) | (DailyAlert.phone == phone_clean)
                ).update({"is_active": False})
                db.commit()

            msg_hi = "अलर्ट रद्द किया गया। आप कभी भी फिर से अलर्ट शुरू कर सकते हैं।"
            msg_en = "Daily alert deactivated. You can re-enable anytime from the home screen."

        return AlertResponse(
            success=True,
            message=msg_en,
            message_hi=msg_hi,
            crop=crop_clean,
            district=district_clean,
            enabled=request.enabled,
            scheduled_time="08:00 AM",
            delivery_channel="WhatsApp & Audio Message"
        )
