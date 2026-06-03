"""Application configuration loaded from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  """Runtime settings for the backend service."""

  app_env: str = "development"
  app_secret_key: str = ""
  frontend_url: str = "http://localhost:3000"
  database_url: str = "postgresql+asyncpg://postgres:postgres@postgres:5432/instareply"
  upstash_redis_url: str = "redis://redis:6379/0"
  jwt_secret_key: str = ""
  jwt_algorithm: str = "HS256"
  jwt_access_token_expire_minutes: int = 15
  jwt_refresh_token_expire_days: int = 7
  google_client_id: str = ""
  meta_app_id: str = ""
  meta_app_secret: str = ""
  meta_webhook_verify_token: str = ""
  meta_api_version: str = "v21.0"
  fernet_key: str = ""
  gemini_api_key: str = ""
  openai_api_key: str = ""
  stripe_secret_key: str = ""
  stripe_webhook_secret: str = ""
  razorpay_key_id: str = ""
  razorpay_key_secret: str = ""

  model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
