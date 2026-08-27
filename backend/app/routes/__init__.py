from app.routes.health import router as health_router
from app.routes.auth import router as auth_router
from app.routes.farming import router as farming_router
from app.routes.conversation import router as conversation_router
from app.routes.mandi import router as mandi_router
from app.routes.advice import router as advice_router
from app.routes.trader import router as trader_router
from app.routes.alerts import router as alerts_router
from app.routes.voice import router as voice_router
from app.routes.advisory import router as advisory_router

__all__ = [
    "health_router",
    "auth_router",
    "farming_router",
    "conversation_router",
    "mandi_router",
    "advice_router",
    "trader_router",
    "alerts_router",
    "voice_router",
    "advisory_router",
]
