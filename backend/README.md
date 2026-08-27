# 🌾 Kisaan Marg - Production Backend & Database Layer

Production-ready **FastAPI** backend and **PostgreSQL / SQLAlchemy / Alembic** database layer for **Kisaan Marg** (किसान मार्ग) — an agriculture-focused AI voice assistant and market advisory platform designed for Indian farmers.

---

## 🏗️ Architecture & Technology Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.10+)
- **Database**: PostgreSQL (with zero-configuration SQLite automatic fallback for instant local execution)
- **ORM**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/)
- **Migrations**: [Alembic](https://alembic.sqlalchemy.org/)
- **Validation**: [Pydantic v2](https://docs.pydantic.dev/) & Pydantic-Settings
- **Authentication**: JWT (JSON Web Tokens) with Bcrypt password hashing
- **Server**: [Uvicorn](https://www.uvicorn.org/) ASGI Server
- **CORS**: Configured for React + Vite frontend (`http://localhost:3000`, `http://localhost:5173`)

---

## 📁 Directory Structure

```
backend/
├── alembic/                     # Database Migrations
│   ├── env.py                   # Alembic environment & metadata link
│   ├── script.py.mako           # Migration template
│   └── versions/
│       └── 0001_initial_database.py # Baseline PostgreSQL schema migration
├── alembic.ini                  # Alembic configuration
│
├── app/
│   ├── main.py                  # FastAPI app, CORS, lifespans, router mounts
│   ├── database.py              # SQLAlchemy engine, connection pool & session dependency
│   ├── config.py                # Discrete DB parameters & Pydantic settings
│   │
│   ├── auth/                    # Security & JWT Authentication
│   │   ├── __init__.py
│   │   ├── jwt.py               # Token creation, decoding, get_current_user
│   │   └── security.py          # Bcrypt password hashing
│   │
│   ├── models/                  # SQLAlchemy ORM Models
│   │   ├── __init__.py
│   │   ├── user.py              # User & FarmerProfile
│   │   ├── farming.py           # FarmingRecord (crop lifecycle & yield tracking)
│   │   ├── conversation.py      # ConversationSession & ChatMessage (AI dialogue logs)
│   │   ├── mandi.py             # Mandi, Commodity, MandiPrice
│   │   ├── advice.py            # RouteQuery, AdviceResult
│   │   ├── trader.py            # TraderEvaluation
│   │   └── alert.py             # DailyAlert, NotificationLog
│   │
│   ├── schemas/                 # Pydantic Request/Response Schemas
│   │   ├── __init__.py
│   │   ├── user.py              # Auth & profile schemas
│   │   ├── farming.py           # Farming records CRUD schemas
│   │   ├── conversation.py      # AI dialogue & message schemas
│   │   ├── mandi.py             # Price queries & responses
│   │   ├── advice.py            # Market recommendation schemas
│   │   ├── trader.py            # Trader evaluation & bargaining schemas
│   │   ├── alert.py             # Alert subscription schemas
│   │   ├── voice.py             # Voice intent parsing schemas
│   │   └── advisory.py          # Weather & crop tip schemas
│   │
│   ├── routes/                  # API Routers (Mounted under /api)
│   │   ├── __init__.py
│   │   ├── health.py            # GET  /api/health
│   │   ├── auth.py              # POST /api/auth/register, POST /api/auth/login, GET /api/auth/me, PUT /api/auth/profile
│   │   ├── farming.py           # CRUD /api/farming/records
│   │   ├── conversation.py      # CRUD /api/conversation/sessions, POST messages
│   │   ├── mandi.py             # POST /api/mandi/prices, GET /api/mandi/list, GET /api/mandi/commodities
│   │   ├── advice.py            # POST /api/advice/recommend, GET /api/advice/history
│   │   ├── trader.py            # POST /api/trader/evaluate, POST /api/trader/bargaining-advice
│   │   ├── alerts.py            # POST /api/alerts/subscribe, GET /api/alerts/my-alerts
│   │   ├── voice.py             # POST /api/voice/process-intent
│   │   └── advisory.py          # GET  /api/advisory/weather, GET /api/advisory/crop
│   │
│   └── services/                # Core Business Logic Layer
│       ├── __init__.py
│       ├── mandi_service.py     # Price lookups & freight calculation
│       ├── advice_service.py    # Route optimization & spoken script generation
│       ├── trader_service.py    # Middleman benchmarking & bargaining scripts
│       ├── alert_service.py     # Alert subscription management
│       ├── voice_ai_service.py  # Hindi/Hinglish speech intent parser
│       └── seed_data.py         # Preloaded Maharashtra mandis & prices
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Environment Variables (`.env`)

Configure your PostgreSQL database and JWT settings:

```env
# Application Configuration
APP_NAME=Kisaan Marg AI Backend
APP_ENV=development
DEBUG=True
API_V1_STR=/api

# Server
HOST=0.0.0.0
PORT=8000

# PostgreSQL Database
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/kisaan_marg_db
DATABASE_NAME=kisaan_marg_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Security & JWT
SECRET_KEY=kisaan_marg_super_secret_jwt_key_sih2024_change_in_production_998877
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:5173,http://127.0.0.1:3000,http://127.0.0.1:5173
```

---

## 🗄️ Database Migrations (Alembic)

```bash
# Navigate to the backend directory
cd backend

# Run pending migrations
alembic upgrade head

# Generate a new migration after editing models
alembic revision --autogenerate -m "add new field"
```

---

## 🚀 Running the Backend

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run migrations
alembic upgrade head

# 3. Start FastAPI server with hot-reload
uvicorn app.main:app --reload --port 8000
```

---

## 📖 Interactive API Documentation

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc UI**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
