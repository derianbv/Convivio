"""
PostgreSQL Database Connection Handler
Placeholder for managing database connections
"""
from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
from config.database import DatabaseConfig


class DatabaseConnection:
    """Handles PostgreSQL database connections"""
    
    _engine = None
    
    @classmethod
    def get_engine(cls):
        """Get or create database engine"""
        if cls._engine is None:
            cls._engine = create_engine(
                DatabaseConfig.url,
                echo=DatabaseConfig.echo,
                poolclass=QueuePool,
                pool_size=DatabaseConfig.pool_size,
                max_overflow=DatabaseConfig.max_overflow,
                pool_timeout=DatabaseConfig.pool_timeout,
                pool_recycle=DatabaseConfig.pool_recycle,
            )
        return cls._engine
    
    @classmethod
    def test_connection(cls):
        """Test the database connection"""
        try:
            engine = cls.get_engine()
            with engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))
                print("Database connection successful!")
                return True
        except Exception as e:
            print(f"Database connection failed: {e}")
            return False
    
    @classmethod
    def dispose(cls):
        """Dispose of the engine connection pool"""
        if cls._engine is not None:
            cls._engine.dispose()
            cls._engine = None
