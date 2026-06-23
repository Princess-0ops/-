import os
from typing import Optional, List
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Core Settings
    BOT_TOKEN: Optional[str] = Field(None, env="BOT_TOKEN")
    DATABASE_URL: Optional[str] = Field(None, env="DATABASE_URL")
    API_KEY: Optional[str] = Field(None, env="API_KEY")
    BASE_URL: str = Field("https://api.openai.com/v1/chat/completions", env="BASE_URL")
    MODEL: str = Field("gpt-4o-mini", env="MODEL")

    # Admin Settings
    OWNER_ID: Optional[int] = Field(None, env="OWNER_ID")
    ADMIN_LIST: str = Field("", env="ADMIN_LIST")

    # Bot Information
    BOT_NAME: str = Field("سـنـفورة ٱلـبـَنـات", env="BOT_NAME")
    BOT_DESCRIPTION: str = Field("بوت ذكي متقدم يدعم شخصيات متعددة والذكاء الاصطناعي", env="BOT_DESCRIPTION")
    WELCOME_MESSAGE: str = Field(
        "مرحباً بك! أنا سـنـفورة ٱلـبـَنـات، بوت ذكي متقدم. اختر شخصية للبدء.",
        env="WELCOME_MESSAGE"
    )

    # Rate Limiting
    RATE_LIMIT_MESSAGES: int = Field(30, env="RATE_LIMIT_MESSAGES")
    RATE_LIMIT_WINDOW: int = Field(60, env="RATE_LIMIT_WINDOW")
    FREE_MESSAGES: int = Field(100, env="FREE_MESSAGES")
    MAINTENANCE_MODE: bool = Field(False, env="MAINTENANCE_MODE")

    # Cache & Storage
    REDIS_URL: Optional[str] = Field(None, env="REDIS_URL")

    # Logging
    LOG_LEVEL: str = Field("INFO", env="LOG_LEVEL")
    LOG_FILE: str = Field("logs/bot.log", env="LOG_FILE")

    # New Environment Variables for Railway
    TZ: str = Field("Asia/Amman", env="TZ")
    MAX_CONCURRENT_TASKS: int = Field(2, env="MAX_CONCURRENT_TASKS")
    START_FROM_LATEST: bool = Field(True, env="START_FROM_LATEST")

    class Config:
        env_file = ".env"
        extra = "allow"

    @property
    def admin_ids(self) -> List[int]:
        if not self.ADMIN_LIST:
            return []
        try:
            return [int(x.strip()) for x in self.ADMIN_LIST.split(",") if x.strip()]
        except ValueError:
            return []

    @property
    def async_database_url(self) -> str:
        url = self.DATABASE_URL or ""
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql+asyncpg://", 1)
        elif url.startswith("postgresql://") and "+asyncpg" not in url:
            url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
        return url


settings = Settings()
