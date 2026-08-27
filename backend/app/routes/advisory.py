from datetime import date, timedelta
from typing import Optional
from fastapi import APIRouter, Query
from app.schemas.advisory import WeatherAdvisoryResponse, CropAdvisoryResponse

router = APIRouter(prefix="/advisory", tags=["Agricultural & Weather Advisory"])


@router.get("/weather", response_model=WeatherAdvisoryResponse, summary="Weather & Harvest Advisory")
def get_weather_advisory(district: str = Query("Nashik", description="Farmer district")):
    """
    Get 3-day weather forecast and harvesting impact advisory for farmers.
    """
    today = date.today()
    return WeatherAdvisoryResponse(
        district=district,
        state="Maharashtra",
        current_temp_celsius=28.5,
        condition="Clear & Sunny",
        condition_hi="साफ और धूपदार",
        harvest_recommendation="Ideal for tomato picking and mandi dispatch before 11:00 AM.",
        harvest_recommendation_hi="टमाटर तोड़ने और सुबह 11:00 बजे से पहले मंडी भेजने के लिए उत्तम मौसम।",
        forecast=[
            {
                "date": str(today),
                "condition": "Sunny",
                "condition_hi": "धूप",
                "temp_max": 31.0,
                "temp_min": 19.5,
                "rainfall_prob_percent": 5,
                "humidity_percent": 45,
                "impact_on_harvest": "Safe for loading & transport",
                "impact_on_harvest_hi": "गाड़ी में लोडिंग और परिवहन के लिए सुरक्षित",
            },
            {
                "date": str(today + timedelta(days=1)),
                "condition": "Partly Cloudy",
                "condition_hi": "आंशिक बादल",
                "temp_max": 30.0,
                "temp_min": 20.0,
                "rainfall_prob_percent": 15,
                "humidity_percent": 52,
                "impact_on_harvest": "Good harvesting conditions",
                "impact_on_harvest_hi": "कटाई के लिए अनुकूल स्थिति",
            },
            {
                "date": str(today + timedelta(days=2)),
                "condition": "Light Breeze",
                "condition_hi": "हल्की हवा",
                "temp_max": 29.5,
                "temp_min": 18.0,
                "rainfall_prob_percent": 10,
                "humidity_percent": 48,
                "impact_on_harvest": "Favorable market transit",
                "impact_on_harvest_hi": "मंडी तक माल ले जाने के लिए उत्तम",
            },
        ]
    )


@router.get("/crop", response_model=CropAdvisoryResponse, summary="Crop Advisory & Price Trends")
def get_crop_advisory(
    crop: str = Query("Tomato", description="Crop name"),
    district: str = Query("Nashik", description="District")
):
    """
    Get crop-specific market outlook, price trend predictions, and harvest storage tips.
    """
    return CropAdvisoryResponse(
        crop=crop,
        crop_hindi="टमाटर" if crop.lower() == "tomato" else "फसल",
        district=district,
        season="Kharif / Late Summer",
        market_trend="Upward (+₹2 to ₹3/kg expected over next 4 days due to higher Mumbai demand)",
        market_trend_hi="तेजी का रुख (मुंबई बाज़ार में मांग बढ़ने से अगले 4 दिनों में ₹2 से ₹3 प्रति किलो बढ़ने का अनुमान)",
        storage_advice="Avoid piling crates in direct sunlight; ensure crates are stacked with aeration slots.",
        storage_advice_hi="क्रेट्स को सीधी धूप से बचाएं; हवादार जगह पर ही क्रेट्स की स्टेकिंग करें।",
        tips=[
            {
                "topic": "Grading",
                "topic_hi": "ग्रेडिंग व छंटाई",
                "advice": "Grade tomatoes by color and firmness into Grade A (firm red) and Grade B (semi-ripe) for 15-20% higher pricing at Lasalgaon.",
                "advice_hi": "लासलगाँव में 15-20% बेहतर भाव के लिए पके लाल और अर्ध-पके फलों की अलग-अलग छंटाई करें।",
                "severity": "tip"
            },
            {
                "topic": "Dispatch Timing",
                "topic_hi": "मंडी पहुँचने का समय",
                "advice": "Reach the mandi auction yard between 5:30 AM and 7:00 AM for peak bidder participation.",
                "advice_hi": "अधिकतम खरीदारों की नीलामी में शामिल होने के लिए सुबह 5:30 से 7:00 बजे के बीच मंडी पहुँचें।",
                "severity": "normal"
            },
            {
                "topic": "Moisture Control",
                "topic_hi": "नमी नियंत्रण",
                "advice": "Do not harvest immediately after overhead sprinkling or morning dew to prevent post-harvest rot.",
                "advice_hi": "सुबह की ओस या पानी देने के तुरंत बाद फल न तोड़ें ताकि फल खराब न हों।",
                "severity": "warning"
            }
        ]
    )
