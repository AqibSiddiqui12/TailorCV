# config.py
# Purpose: environment variables + app-wide settings, loaded once.

# class Settings(BaseSettings):
#     - Fields: anthropic_api_key, redis_url, allowed_origin (chrome-extension://<id>),
#       rate_limit_per_minute, max_upload_mb, claude_model, claude_max_tokens, environment
#     - model_config = SettingsConfigDict(env_file=".env")

# def get_settings() -> Settings:
#     - @lru_cache-wrapped singleton so .env is parsed only once
#     - Imported via Depends(get_settings) wherever config is needed
