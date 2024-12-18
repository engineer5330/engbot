from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import  AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import select, update, delete
from sqlalchemy import BigInteger, String

import sqlite3

engine = create_async_engine(url="sqlite+aiosqlite:///engineeriysDB.sqlite3")
async_session = async_sessionmaker(engine)
class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
