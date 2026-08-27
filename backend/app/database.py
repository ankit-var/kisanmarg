import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

logger = logging.getLogger("kisaan_marg.database")

db_url = settings.DATABASE_URL
connect_args = {}

if db_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
    engine = create_engine(
        db_url,
        connect_args=connect_args,
        echo=False
    )
    logger.info(f"Initialized SQLite database engine: {db_url}")
else:
    try:
        # Probe PostgreSQL connection
        test_engine = create_engine(
            db_url,
            pool_pre_ping=True,
            pool_size=10,
            max_overflow=20,
            echo=False
        )
        with test_engine.connect() as conn:
            pass
        engine = test_engine
        logger.info("Successfully connected to PostgreSQL database.")
    except Exception as e:
        logger.warning(f"PostgreSQL connection to {db_url} failed ({e}). Falling back to local SQLite database.")
        db_url = "sqlite:///./kisaan_marg.db"
        connect_args = {"check_same_thread": False}
        engine = create_engine(db_url, connect_args=connect_args, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    FastAPI dependency that yields a SQLAlchemy database session
    and ensures clean closing after request completion.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
