from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

# crea la conexión con postgres
engine = create_async_engine(settings.database_url, echo=True)

# genera sesiones con la configuración correcta
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


# generador sesiones para FastAPI
async def get_db() -> AsyncSession:
    async with AsyncSession() as session:
        yield session
