"""
PostgreSQL Database Configuration
Placeholder for database connection settings
"""
import os
from typing import Optional

# Environment variables (use .env file in production)
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "convivio_db")

# Database URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Connection pool settings
POOL_SIZE = 5
MAX_OVERFLOW = 10
POOL_TIMEOUT = 30
POOL_RECYCLE = 3600  # Recycle connections every hour

# Database configuration
class DatabaseConfig:
    """Database configuration class"""
    url: str = DATABASE_URL
    echo: bool = True  # Set to False in production
    pool_size: int = POOL_SIZE
    max_overflow: int = MAX_OVERFLOW
    pool_timeout: int = POOL_TIMEOUT
    pool_recycle: int = POOL_RECYCLE
