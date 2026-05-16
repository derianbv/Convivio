"""
API Middleware
Placeholder for CORS, error handling, and request/response middleware
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.api import APIConfig


def setup_middleware(app: FastAPI):
    """Setup all middleware for the FastAPI application"""
    
    # CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=APIConfig.cors_origins,
        allow_credentials=True,
        allow_methods=APIConfig.cors_origins,
        allow_headers=["*"],
    )
    
    # TODO: Add custom middleware for:
    # - Request/response logging
    # - Error handling
    # - Authentication/Authorization
    # - Request validation
    
    return app


def setup_error_handlers(app: FastAPI):
    """Setup error handlers for common exceptions"""
    
    @app.exception_handler(ValueError)
    async def value_error_handler(request, exc):
        """Handle ValueError"""
        return {
            "error": "Invalid value",
            "message": str(exc)
        }
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request, exc):
        """Handle general exceptions"""
        return {
            "error": "Internal server error",
            "message": str(exc)
        }
