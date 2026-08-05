from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    anthropic_api_key: str
    claude_model: str = "claude-3-5-sonnet"



@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()