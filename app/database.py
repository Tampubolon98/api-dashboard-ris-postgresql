from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings
from urllib.parse import quote_plus

db_user = quote_plus(settings.db_username_ris)
db_password = quote_plus(settings.db_password_ris)

# Create an async database URL without the query parameters
ASYNC_DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{db_user}:{db_password}@"
    f"{settings.db_host_ris}:"
    f"{settings.db_port_ris}/"
    f"{settings.db_database_ris}"
)

# Create an async SQLAlchemy engine with SSL configuration
engine = create_async_engine(
    ASYNC_DATABASE_URL, 
    echo=True,
    pool_pre_ping=True,
    pool_recycle=300
)

# Create a session factory for creating database sessions
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Create a base class for declarative models
Base = declarative_base()

# Dependency to get an async database session
async def get_db():
    async with async_session() as session:
        try:
            yield session
            # await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()