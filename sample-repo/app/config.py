"""Application configuration."""

DATABASE_URL = "sqlite:///./library.db"
API_PREFIX = "/api/v1"
CRON_OVERDUE_CHECK = "0 9 * * *"  # daily at 09:00
