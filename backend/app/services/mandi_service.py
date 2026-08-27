from datetime import date
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from app.models.mandi import Mandi, Commodity, MandiPrice
from app.schemas.mandi import MandiPriceQuery, MandiPriceResponse, MandiInfo

# Approximate road distance matrix between districts and key mandis (in kilometers)
DISTRICT_MANDI_DISTANCES = {
    "Nashik": {
        "Lasalgaon Mandi": 42.0,
        "Pimpalgaon Baswant Mandi": 28.0,
        "Nashik Main APMC (Dindori Road)": 8.0,
        "Pune Gultekdi Market Yard": 210.0,
        "Rahata APMC Mandi": 88.0,
        "Solapur APMC Market": 390.0,
    },
    "Pune": {
        "Pune Gultekdi Market Yard": 6.0,
        "Lasalgaon Mandi": 215.0,
        "Pimpalgaon Baswant Mandi": 230.0,
        "Nashik Main APMC (Dindori Road)": 210.0,
        "Rahata APMC Mandi": 180.0,
        "Solapur APMC Market": 250.0,
    },
    "Ahmednagar": {
        "Rahata APMC Mandi": 45.0,
        "Lasalgaon Mandi": 110.0,
        "Pimpalgaon Baswant Mandi": 125.0,
        "Nashik Main APMC (Dindori Road)": 140.0,
        "Pune Gultekdi Market Yard": 120.0,
        "Solapur APMC Market": 220.0,
    },
    "Solapur": {
        "Solapur APMC Market": 10.0,
        "Pune Gultekdi Market Yard": 250.0,
        "Rahata APMC Mandi": 280.0,
        "Lasalgaon Mandi": 390.0,
        "Pimpalgaon Baswant Mandi": 410.0,
        "Nashik Main APMC (Dindori Road)": 400.0,
    },
}

DEFAULT_DISTANCES = {
    "Lasalgaon Mandi": 42.0,
    "Pimpalgaon Baswant Mandi": 28.0,
    "Nashik Main APMC (Dindori Road)": 8.0,
    "Pune Gultekdi Market Yard": 150.0,
    "Rahata APMC Mandi": 75.0,
    "Solapur APMC Market": 280.0,
}


def parse_quantity_kg(quantity_input: Any) -> float:
    """Safely parse input like 500, '500 Kg', '1000kg' into float kilograms."""
    if isinstance(quantity_input, (int, float)):
        return float(quantity_input)
    if isinstance(quantity_input, str):
        cleaned = "".join([c for c in quantity_input if c.isdigit() or c == "."])
        try:
            return float(cleaned) if cleaned else 500.0
        except ValueError:
            return 500.0
    return 500.0


def calculate_transport_cost(distance_km: float, quantity_kg: float) -> Dict[str, float]:
    """
    Calculate rural agricultural transport logistics cost:
    - Base vehicle rental fee (e.g. Piaggio Ape / Tata Ace tempo): ₹300
    - Per km freight rate: ₹25/km for up to 1000 kg, scaled by quantity.
    - Returns total logistics cost and per kg cost impact.
    """
    base_charge = 250.0
    rate_per_km = 22.0
    
    # Scale slightly for large harvest loads (e.g. > 1000 kg)
    load_factor = max(1.0, quantity_kg / 1000.0)
    total_cost = base_charge + (distance_km * rate_per_km * (0.8 + 0.2 * load_factor))
    cost_per_kg = round(total_cost / max(1.0, quantity_kg), 2)
    
    return {
        "total_cost": round(total_cost, 2),
        "cost_per_kg": cost_per_kg,
    }


def get_mandi_distance(district: str, mandi_name: str) -> float:
    """Retrieve road distance in km between district and mandi."""
    district_table = DISTRICT_MANDI_DISTANCES.get(district, DEFAULT_DISTANCES)
    return district_table.get(mandi_name, DEFAULT_DISTANCES.get(mandi_name, 50.0))


class MandiService:
    @staticmethod
    def get_prices(db: Session, query: MandiPriceQuery) -> MandiPriceResponse:
        crop_clean = query.crop.strip().lower()
        district_clean = (query.district or "Nashik").strip()
        
        # Match Commodity
        commodity = db.query(Commodity).filter(
            (Commodity.name.ilike(f"%{crop_clean}%")) | (Commodity.hindi_name.ilike(f"%{crop_clean}%"))
        ).first()

        if not commodity:
            commodity = db.query(Commodity).filter(Commodity.name == "Tomato").first()

        commodity_id = commodity.id if commodity else 1
        crop_name = commodity.name if commodity else "Tomato"
        crop_hindi = commodity.hindi_name if commodity else "टमाटर"

        # Query all active mandis with prices
        prices = db.query(MandiPrice).join(Mandi).filter(
            MandiPrice.commodity_id == commodity_id,
            Mandi.is_active == True
        ).all()

        mandi_list: List[MandiInfo] = []
        for p in prices:
            dist = get_mandi_distance(district_clean, p.mandi.name)
            mandi_list.append(
                MandiInfo(
                    id=p.mandi.id,
                    name=p.mandi.name,
                    hindi_name=p.mandi.hindi_name,
                    district=p.mandi.district,
                    state=p.mandi.state,
                    distance_km=dist,
                    price_per_kg=p.price_per_kg,
                    min_price_quintal=p.min_price_quintal,
                    max_price_quintal=p.max_price_quintal,
                    modal_price_quintal=p.modal_price_quintal,
                    grade=p.grade or "Grade A",
                    price_date=p.price_date
                )
            )

        # Sort by distance first, then price
        mandi_list.sort(key=lambda x: (x.distance_km or 999))

        return MandiPriceResponse(
            crop=crop_name,
            crop_hindi=crop_hindi,
            district=district_clean,
            queried_at=str(date.today()),
            mandis_count=len(mandi_list),
            data=mandi_list
        )
