# todo_app/database.py
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from .config import get_settings
from contextlib import asynccontextmanager

settings = get_settings()
# Use asyncpg driver for async engine
async_engine = create_async_engine(
    settings.database_url.replace("postgresql://", "postgresql+asyncpg://"), echo=True
)

async def create_db_and_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# @asynccontextmanager
async def get_session():
    async with AsyncSession(async_engine) as session:
        yield session