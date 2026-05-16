"""
SQLAlchemy Session Management
Placeholder for session factory and dependency injection
"""
from typing import Generator
from sqlalchemy.orm import sessionmaker, Session
from infrastructure.db_connection import DatabaseConnection


# Create session factory
SessionLocal = sessionmaker(
    bind=DatabaseConnection.get_engine(),
    autocommit=False,
    autoflush=False,
)


def get_db() -> Generator[Session, None, None]:
    """
    Dependency for FastAPI to get database session
    Usage in routes: def some_endpoint(db: Session = Depends(get_db))
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DatabaseSession:
    """Context manager for database sessions"""
    
    def __enter__(self) -> Session:
        """Enter context manager"""
        self.db = SessionLocal()
        return self.db
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager"""
        self.db.close()
