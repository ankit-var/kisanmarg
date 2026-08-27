from typing import Optional
from sqlalchemy.orm import Session
from app.models.mandi import MandiPrice, Commodity
from app.models.trader import TraderEvaluation
from app.models.user import User
from app.schemas.trader import (
    TraderOfferRequest,
    TraderOfferResponse,
    BargainingRequest,
    BargainingResponse,
)


class TraderService:
    @staticmethod
    def evaluate_offer(
        db: Session,
        request: TraderOfferRequest,
        current_user: Optional[User] = None
    ) -> TraderOfferResponse:
        crop_clean = request.crop.strip().lower()
        district_clean = (request.district or "Nashik").strip()
        offer = float(request.offerPrice)

        # 1. Match Commodity & Prevailing Market Benchmark
        commodity = db.query(Commodity).filter(
            (Commodity.name.ilike(f"%{crop_clean}%")) | (Commodity.hindi_name.ilike(f"%{crop_clean}%"))
        ).first()

        commodity_id = commodity.id if commodity else 1
        crop_name = commodity.name if commodity else "Tomato"
        crop_hindi = commodity.hindi_name if commodity else "टमाटर"

        # Benchmark modal price
        avg_price = db.query(MandiPrice).filter(
            MandiPrice.commodity_id == commodity_id
        ).first()

        benchmark_price = avg_price.price_per_kg if avg_price else 23.0

        # Calculate fair target price range
        # Traders usually buy at farm-gate at ~70-75% of regional wholesale net price
        fair_min_target = round(benchmark_price * 0.70, 0)
        fair_max_target = round(benchmark_price * 0.80, 0)

        # Ensure sensible lower bound
        if fair_min_target < 16.0:
            fair_min_target = 16.0
            fair_max_target = 18.0

        is_fair = offer >= fair_min_target

        if offer < fair_min_target:
            verdict = "कम भाव"
            verdict_en = "Low Offer"
            warning_text = f"₹{int(offer)} प्रति किलो कम है. व्यापारी से कम-से-कम ₹{int(fair_min_target)} माँगिए."
            warning_text_en = f"₹{int(offer)}/kg is below market average. Ask the trader for at least ₹{int(fair_min_target)}/kg."
        else:
            verdict = "उचित भाव"
            verdict_en = "Fair Offer"
            warning_text = f"₹{int(offer)} प्रति किलो बाज़ार के अनुसार सही भाव है."
            warning_text_en = f"₹{int(offer)}/kg is a fair rate matching current wholesale benchmarks."

        script_preview = f"\"पास की मंडी में भाव ₹{int(benchmark_price)} है। मुझे कम-से-कम ₹{int(fair_min_target)} से ₹{int(fair_max_target)} मिलना चाहिए।\""

        # Persist evaluation record
        try:
            record = TraderEvaluation(
                user_id=current_user.id if current_user else None,
                crop=crop_name,
                district=district_clean,
                offer_price_per_kg=offer,
                benchmark_mandi_price=benchmark_price,
                target_price_per_kg=fair_min_target,
                target_price_max=fair_max_target,
                is_fair_price=is_fair,
                verdict=verdict,
                warning_text_hi=warning_text,
                warning_text_en=warning_text_en,
                bargaining_script_hi=script_preview,
                bargaining_script_en=f"Market rate is ₹{benchmark_price}/kg. I should get at least ₹{fair_min_target} to ₹{fair_max_target}/kg.",
            )
            db.add(record)
            db.commit()
        except Exception:
            db.rollback()

        return TraderOfferResponse(
            success=True,
            crop=crop_name,
            crop_hindi=crop_hindi,
            offer_price=offer,
            district=district_clean,
            benchmark_mandi_price=benchmark_price,
            target_price=fair_min_target,
            target_price_max=fair_max_target,
            is_fair_price=is_fair,
            verdict=verdict,
            verdict_en=verdict_en,
            warning_text=warning_text,
            warning_text_en=warning_text_en,
            bargaining_script_preview=script_preview
        )

    @staticmethod
    def get_bargaining_advice(request: BargainingRequest) -> BargainingResponse:
        offer = float(request.offerPrice)
        target = float(request.targetPrice or 16.0)
        target_max = target + 2.0
        crop = request.crop or "tomato"

        script_hi = f"\"पास की मंडी में भाव अधिक है। मुझे कम-से-कम ₹{int(target)} से ₹{int(target_max)} प्रति किलो मिलना चाहिए।\""
        script_en = f"\"Wholesale market rates are currently higher. I should receive at least ₹{int(target)} to ₹{int(target_max)} per kg.\""

        tips = [
            "व्यापारी को बताएं कि आपने आज की लासलगाँव मंडी का ताज़ा भाव चेक किया है।",
            "ग्रेड-A टमाटर की अच्छी क्वालिटी और कम कटाई खराबी का उल्लेख करें।",
            "यदि व्यापारी सहमत न हो, तो समूह के अन्य किसानों के साथ मिलकर सीधे मंडी में ले जाने का विकल्प रखें।"
        ]

        return BargainingResponse(
            success=True,
            crop=crop,
            offer_price=offer,
            target_price=target,
            target_price_max=target_max,
            script=script_hi,
            script_en=script_en,
            audio_duration=12.0,
            negotiation_tips=tips
        )
