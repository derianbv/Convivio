"""
API Server Configuration
Placeholder for API server settings
"""
import os

# API Configuration
API_TITLE = "Convivio API"
API_DESCRIPTION = "Backend API for Convivio property management system"
API_VERSION = "0.1.0"

# Server settings
SERVER_HOST = os.getenv("API_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("API_PORT", "8000"))
DEBUG = os.getenv("DEBUG", "True") == "True"

# CORS settings for React frontend
CORS_ORIGINS = [
    "http://localhost:3000",      # React dev server
    "http://127.0.0.1:3000",
    "http://localhost:8080",       # Alternative dev port
    # Add production URLs here
    # "https://yourdomain.com",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"]
CORS_ALLOW_HEADERS = ["Content-Type", "Authorization"]

class APIConfig:
    """API configuration class"""
    title: str = API_TITLE
    description: str = API_DESCRIPTION
    version: str = API_VERSION
    host: str = SERVER_HOST
    port: int = SERVER_PORT
    debug: bool = DEBUG
    cors_origins: list = CORS_ORIGINS
