"""
Convivio Backend Application
Main entry point for FastAPI server
Run with: python app.py
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.middleware import setup_middleware, setup_error_handlers
from api.routes import router
from config.api import APIConfig
from infrastructure.db_connection import DatabaseConnection


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application startup and shutdown"""
    # Startup
    print("Starting Convivio API...")
    if DatabaseConnection.test_connection():
        print("API ready!")
    else:
        print("Warning: Database connection failed. Check your configuration.")
    yield
    # Shutdown
    print("Shutting down Convivio API...")
    DatabaseConnection.dispose()


def create_app() -> FastAPI:
    """Create and configure the FastAPI application"""
    
    app = FastAPI(
        title=APIConfig.title,
        description=APIConfig.description,
        version=APIConfig.version,
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        lifespan=lifespan,
    )
    
    # Setup middleware
    setup_middleware(app)
    
    # Setup error handlers
    setup_error_handlers(app)
    
    # Include routes
    app.include_router(router)
    
    return app


# Create app instance
app = create_app()


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app:app",
        host=APIConfig.host,
        port=APIConfig.port,
        reload=APIConfig.debug,
        log_level="info"
    )
