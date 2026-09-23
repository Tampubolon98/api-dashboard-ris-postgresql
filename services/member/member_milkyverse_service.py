from repositories.member.member_milkyverse_repository import get_pembayaran_member_repository
from app.database import get_db_milkyverse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

async def get_pembayaran_members_service(db_milkyverse: AsyncSession, db: AsyncSession, compid):
    try:
        result = await get_pembayaran_member_repository(db_milkyverse, db, compid)

        if not result:
            return {
                "status": False,
                "message": "Data tidak ditemukan"
            }

        return {
            "status": True,
            "message": "OK",
            "total_data": len(result),
            "data": result
        }
    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }