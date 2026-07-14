"""
Configuration management for the application.
"""
from typing import List

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """
    Application settings and configuration.
    Loads from environment variables and .env file.
    """

    # Application
    APP_NAME: str = "Count-Me-In"
    DEBUG: bool = Field(default=False, alias="DEBUG")
    ENVIRONMENT: str = Field(default="development", alias="FLASK_ENV")
    SECRET_KEY: str = Field(default="your-secret-key-change-in-production")
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 5000
    ALLOWED_HOSTS: List[str] = ["*"]

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://localhost:5173",
    ]

    # Database
    DATABASE_URL: str = Field(
        default="postgresql://user:password@localhost:5432/count_me_in"
    )
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20
    DB_ECHO: bool = False  # Set to True for SQL query logging

    # Redis
    REDIS_URL: str = Field(default="redis://localhost:6379/0")
    REDIS_TIMEOUT: int = 5

    # JWT
    JWT_SECRET: str = Field(default="your-jwt-secret-change-in-production")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    REFRESH_TOKEN_EXPIRATION_DAYS: int = 7

    # YOLO Model
    MODEL_TYPE: str = "yolov8n"
    MODEL_PATH: str = "models/yolo_v8/best.pt"
    CONFIDENCE_THRESHOLD: float = 0.5
    IOU_THRESHOLD: float = 0.45

    # Edge Configuration
    EDGE_DEVICE: str = "cpu"  # Options: cpu, cuda, tpu
    EDGE_INFERENCE_TIMEOUT: int = 5
    BATCH_SIZE: int = 1

    # Camera Settings
    CAMERA_SOURCE: str = "0"
    VIDEO_FPS: int = 30
    VIDEO_WIDTH: int = 640
    VIDEO_HEIGHT: int = 480
    SKIP_FRAMES: int = 2

    # Occupancy Settings
    MAX_CAPACITY_THRESHOLD: int = 85  # Alert when exceeds % of capacity
    CRITICAL_CAPACITY_THRESHOLD: int = 95
    OCCUPANCY_UPDATE_INTERVAL: int = 5  # seconds

    # Alerts
    ENABLE_ALERTS: bool = True
    ALERT_WEBHOOK_URL: str = ""
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"

    # Pagination
    DEFAULT_PAGE_SIZE: int = 30
    MAX_PAGE_SIZE: int = 100

    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_PER_MINUTE: int = 60

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "allow"


settings = Settings()
