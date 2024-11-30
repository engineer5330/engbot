from apps.db.models import async_session
from apps.db.models import select
from apps.db.models import User


async def AddUsers(tg_id, name, password):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id, name=name, password=password))
            await session.commit()

async def CheckReg(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            return False
        else:
            return True
