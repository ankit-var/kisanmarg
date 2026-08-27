import logging
from datetime import date
from sqlalchemy.orm import Session
from app.models.mandi import Mandi, Commodity, MandiPrice
from app.models.user import User, FarmerProfile
from app.auth.security import get_password_hash

logger = logging.getLogger("kisaan_marg.seed")

# Predefined Commodities
COMMODITIES_DATA = [
    {"name": "Tomato", "hindi_name": "टमाटर", "category": "Vegetables", "unit": "kg"},
    {"name": "Onion", "hindi_name": "प्याज", "category": "Vegetables", "unit": "kg"},
    {"name": "Potato", "hindi_name": "आलू", "category": "Vegetables", "unit": "kg"},
    {"name": "Wheat", "hindi_name": "गेहूँ", "category": "Grains", "unit": "kg"},
    {"name": "Soybean", "hindi_name": "सोयाबीन", "category": "Oilseeds", "unit": "kg"},
]

# Predefined Mandis across Maharashtra
MANDIS_DATA = [
    {
        "name": "Lasalgaon Mandi",
        "hindi_name": "लासलगाँव मंडी",
        "district": "Nashik",
        "state": "Maharashtra",
        "latitude": 20.1472,
        "longitude": 74.2255,
    },
    {
        "name": "Pimpalgaon Baswant Mandi",
        "hindi_name": "पिंपलगांव बसवंत मंडी",
        "district": "Nashik",
        "state": "Maharashtra",
        "latitude": 20.1706,
        "longitude": 73.9847,
    },
    {
        "name": "Nashik Main APMC (Dindori Road)",
        "hindi_name": "नासिक मुख्य मंडी (दिंडोरी रोड)",
        "district": "Nashik",
        "state": "Maharashtra",
        "latitude": 20.0110,
        "longitude": 73.7903,
    },
    {
        "name": "Pune Gultekdi Market Yard",
        "hindi_name": "पुणे गुलटेकडी मार्केट यार्ड",
        "district": "Pune",
        "state": "Maharashtra",
        "latitude": 18.4975,
        "longitude": 73.8647,
    },
    {
        "name": "Rahata APMC Mandi",
        "hindi_name": "राहाता मंडी",
        "district": "Ahmednagar",
        "state": "Maharashtra",
        "latitude": 19.6976,
        "longitude": 74.4842,
    },
    {
        "name": "Solapur APMC Market",
        "hindi_name": "सोलापुर मंडी",
        "district": "Solapur",
        "state": "Maharashtra",
        "latitude": 17.6599,
        "longitude": 75.9064,
    },
]

# Sample Prices per Quintal (100 kg) for Tomato and Onion
# Lasalgaon: ₹2600/quintal (₹26/kg)
# Pimpalgaon: ₹2400/quintal (₹24/kg)
# Nashik Local: ₹2100/quintal (₹21/kg)
# Pune: ₹2700/quintal (₹27/kg)
# Rahata: ₹2200/quintal (₹22/kg)
# Solapur: ₹2000/quintal (₹20/kg)
PRICES_DATA = [
    # Tomato prices
    {"mandi_name": "Lasalgaon Mandi", "commodity_name": "Tomato", "modal": 2600.0, "min": 2200.0, "max": 2800.0, "arrivals": 240.0},
    {"mandi_name": "Pimpalgaon Baswant Mandi", "commodity_name": "Tomato", "modal": 2400.0, "min": 2000.0, "max": 2550.0, "arrivals": 180.0},
    {"mandi_name": "Nashik Main APMC (Dindori Road)", "commodity_name": "Tomato", "modal": 2100.0, "min": 1800.0, "max": 2300.0, "arrivals": 120.0},
    {"mandi_name": "Pune Gultekdi Market Yard", "commodity_name": "Tomato", "modal": 2700.0, "min": 2300.0, "max": 2900.0, "arrivals": 450.0},
    {"mandi_name": "Rahata APMC Mandi", "commodity_name": "Tomato", "modal": 2200.0, "min": 1900.0, "max": 2400.0, "arrivals": 90.0},
    {"mandi_name": "Solapur APMC Market", "commodity_name": "Tomato", "modal": 2000.0, "min": 1700.0, "max": 2200.0, "arrivals": 110.0},

    # Onion prices
    {"mandi_name": "Lasalgaon Mandi", "commodity_name": "Onion", "modal": 2800.0, "min": 2400.0, "max": 3100.0, "arrivals": 800.0},
    {"mandi_name": "Pimpalgaon Baswant Mandi", "commodity_name": "Onion", "modal": 2750.0, "min": 2350.0, "max": 3000.0, "arrivals": 520.0},
    {"mandi_name": "Nashik Main APMC (Dindori Road)", "commodity_name": "Onion", "modal": 2500.0, "min": 2100.0, "max": 2700.0, "arrivals": 300.0},
    {"mandi_name": "Pune Gultekdi Market Yard", "commodity_name": "Onion", "modal": 2900.0, "min": 2500.0, "max": 3200.0, "arrivals": 600.0},
    {"mandi_name": "Rahata APMC Mandi", "commodity_name": "Onion", "modal": 2600.0, "min": 2200.0, "max": 2800.0, "arrivals": 190.0},
    {"mandi_name": "Solapur APMC Market", "commodity_name": "Onion", "modal": 2400.0, "min": 2000.0, "max": 2600.0, "arrivals": 210.0},

    # Potato prices
    {"mandi_name": "Pune Gultekdi Market Yard", "commodity_name": "Potato", "modal": 1800.0, "min": 1500.0, "max": 2000.0, "arrivals": 350.0},
    {"mandi_name": "Nashik Main APMC (Dindori Road)", "commodity_name": "Potato", "modal": 1700.0, "min": 1400.0, "max": 1900.0, "arrivals": 180.0},
]


def seed_database(db: Session):
    """Seed commodities, mandis, baseline prices, and a demo farmer user."""
    try:
        # 1. Seed Commodities
        commodity_map = {}
        for c_data in COMMODITIES_DATA:
            existing = db.query(Commodity).filter(Commodity.name == c_data["name"]).first()
            if not existing:
                comm = Commodity(**c_data)
                db.add(comm)
                db.flush()
                commodity_map[comm.name] = comm
            else:
                commodity_map[existing.name] = existing

        # 2. Seed Mandis
        mandi_map = {}
        for m_data in MANDIS_DATA:
            existing = db.query(Mandi).filter(Mandi.name == m_data["name"]).first()
            if not existing:
                mandi = Mandi(**m_data)
                db.add(mandi)
                db.flush()
                mandi_map[mandi.name] = mandi
            else:
                mandi_map[existing.name] = existing

        # 3. Seed Prices
        today = date.today()
        for p_data in PRICES_DATA:
            mandi = mandi_map.get(p_data["mandi_name"])
            commodity = commodity_map.get(p_data["commodity_name"])
            if mandi and commodity:
                existing_price = db.query(MandiPrice).filter(
                    MandiPrice.mandi_id == mandi.id,
                    MandiPrice.commodity_id == commodity.id,
                    MandiPrice.price_date == today
                ).first()
                if not existing_price:
                    price_entry = MandiPrice(
                        mandi_id=mandi.id,
                        commodity_id=commodity.id,
                        modal_price_quintal=p_data["modal"],
                        min_price_quintal=p_data["min"],
                        max_price_quintal=p_data["max"],
                        price_per_kg=round(p_data["modal"] / 100.0, 2),
                        arrivals_tonnes=p_data["arrivals"],
                        grade="Grade A",
                        price_date=today
                    )
                    db.add(price_entry)

        # 4. Seed Demo Farmer User
        demo_phone = "9876543210"
        demo_user = db.query(User).filter(User.phone == demo_phone).first()
        if not demo_user:
            demo_user = User(
                phone=demo_phone,
                email="kisaan.demo@kisaanmarg.gov.in",
                full_name="रमेश पाटिल (Ramesh Patil)",
                hashed_password=get_password_hash("kisaan123"),
                preferred_language="hi",
                is_active=True,
            )
            db.add(demo_user)
            db.flush()

            profile = FarmerProfile(
                user_id=demo_user.id,
                primary_district="Nashik",
                primary_state="Maharashtra",
                default_crop="Tomato",
                land_size_acres=3.5,
            )
            db.add(profile)

        db.commit()
        logger.info("Database seeding completed successfully.")
    except Exception as e:
        db.rollback()
        logger.error(f"Error seeding database: {e}")
