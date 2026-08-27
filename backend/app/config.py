import os
from typing import List, Union, Optional
from pydantic import validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Kisaan Marg AI Backend"
    APP_ENV: str = "development"
    DEBUG: bool = True
    API_V1_STR: str = "/api"

    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # PostgreSQL Database Settings
    DATABASE_NAME: Optional[str] = "kisaan_marg_db"
    DATABASE_USER: Optional[str] = "postgres"
    DATABASE_PASSWORD: Optional[str] = "postgres"
    DATABASE_HOST: Optional[str] = "localhost"
    DATABASE_PORT: Optional[int] = 5432
    DATABASE_URL: Optional[str] = None

    # JWT Authentication
    SECRET_KEY: str = "kisaan_marg_super_secret_jwt_key_sih2024_change_in_production_998877"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # CORS Settings
    CORS_ORIGINS: Union[List[str], str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]

    # External AI / Voice API Keys
    OPENAI_API_KEY: str = ""
    GEMINI_API_KEY: str = ""
    BHASHINI_API_KEY: str = ""
    WEATHER_API_KEY: str = ""

    @validator("DATABASE_URL", pre=True, always=True)
    def assemble_db_url(cls, v: Optional[str], values: dict) -> str:
        if v and isinstance(v, str) and v.strip():
            return v
        user = values.get("DATABASE_USER")
        password = values.get("DATABASE_PASSWORD")
        host = values.get("DATABASE_HOST")
        port = values.get("DATABASE_PORT")
        db = values.get("DATABASE_NAME")
        if user and host and db:
            return f"postgresql://{user}:{password}@{host}:{port}/{db}"
        return "sqlite:///./kisaan_marg.db"

    @validator("CORS_ORIGINS", pre=True)
    def parse_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str):
            return [i.strip() for i in v.split(",") if i.strip()]
        return v

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"


settings = Settings()
