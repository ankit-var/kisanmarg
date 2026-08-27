import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.config import settings
from app.database import engine, Base, SessionLocal
import app.models  # Ensures all ORM models are registered before create_all
from app.services.seed_data import seed_database
from app.routes import (
    health_router,
    auth_router,
    farming_router,
    conversation_router,
    mandi_router,
    advice_router,
    trader_router,
    alerts_router,
    voice_router,
    advisory_router,
)

# Logging configuration
logging.basicConfig(
    level=logging.INFO if settings.DEBUG else logging.WARNING,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
)
logger = logging.getLogger("kisaan_marg.main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown event management.
    Initializes database tables and seeds initial commodity and mandi data.
    """
    logger.info("Starting up Kisaan Marg AI Backend...")
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables initialized successfully.")
        
        # Seed initial data
        db = SessionLocal()
        try:
            seed_database(db)
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Database initialization error: {e}")

    yield

    logger.info("Shutting down Kisaan Marg AI Backend...")


# Instantiate FastAPI Application
app = FastAPI(
    title=settings.APP_NAME,
    description="""
🌾 **Kisaan Marg AI Assistant Backend**

A production-ready FastAPI backend designed to empower Indian farmers with:
- **Voice-first intelligence**: Hindi & Hinglish agricultural intent processing.
- **Dynamic Mandi & Logistics Engine**: Fair net take-home price calculations after transport freight.
- **Middleman Trader Offer Evaluator**: Benchmarks offers and suggests counter-offer scripts.
- **Agricultural & Farming Records**: Complete lifecycle tracking for sown and harvested crops.
- **AI Conversation Sessions**: Multi-turn dialogue history and voice interaction logs.
- **Daily WhatsApp & Audio Price Alerts**: Scheduled APMC mandi alerts.
- **Crop & Weather Advisory**: Localized harvest timing and weather warnings.
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# Configure CORS for React/Vite Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS if isinstance(settings.CORS_ORIGINS, list) else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Global Exception Handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Format validation errors into clean, readable JSON."""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "message": "Input validation error",
            "errors": exc.errors()
        }
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Catch unhandled exceptions and return consistent JSON."""
    logger.exception(f"Unhandled error processing {request.method} {request.url.path}: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "message": "An internal server error occurred. Please try again later.",
            "detail": str(exc) if settings.DEBUG else None
        }
    )


# Root landing
@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Kisaan Marg AI Backend API",
        "docs": "/docs",
        "health": f"{settings.API_V1_STR}/health",
        "version": "1.0.0"
    }


# Mount API Routers under /api
api_prefix = settings.API_V1_STR  # default "/api"

app.include_router(health_router, prefix=api_prefix)
app.include_router(auth_router, prefix=api_prefix)
app.include_router(farming_router, prefix=api_prefix)
app.include_router(conversation_router, prefix=api_prefix)
app.include_router(mandi_router, prefix=api_prefix)
app.include_router(advice_router, prefix=api_prefix)
app.include_router(trader_router, prefix=api_prefix)
app.include_router(alerts_router, prefix=api_prefix)
app.include_router(voice_router, prefix=api_prefix)
app.include_router(advisory_router, prefix=api_prefix)
