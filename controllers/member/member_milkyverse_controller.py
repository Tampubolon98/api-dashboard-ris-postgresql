from services.member.member_milkyverse_service import get_pembayaran_members_service, get_detail_pembayaran_member_service
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date, datetime
from typing import Optional

async def get_pembayaran_member_controller(db_milkyverse: AsyncSession, db: AsyncSession, comp, id_batch: Optional[str] = None, status: Optional[str] = None, start_date: Optional[date] = None, end_date: Optional[date] = None):
    try:
        data = await get_pembayaran_members_service(db_milkyverse, db, comp, id_batch, status, start_date, end_date)
        return data
    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }
    
async def get_detail_pembayaran_controller(db_milkyverse: AsyncSession, comp, id_batch: str):
    try:
        data = await get_detail_pembayaran_member_service(db_milkyverse, comp, id_batch)
        return data
    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }