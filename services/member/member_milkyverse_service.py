from repositories.member.member_milkyverse_repository import get_pembayaran_member_repository, get_detail_pembayaran_member_repository
from app.database import get_db_milkyverse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from datetime import date, datetime
from typing import Optional

async def get_pembayaran_members_service(db_milkyverse: AsyncSession, db: AsyncSession, compid, id_batch: Optional[str] = None, status: Optional[str] = None, start_date: Optional[date] = None, end_date: Optional[date] = None) -> dict:
    try:
        result = await get_pembayaran_member_repository(db_milkyverse, db, compid, id_batch, status, start_date, end_date)

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
    
async def get_detail_pembayaran_member_service(db_milkyverse: AsyncSession, compid, id_batch: str) -> dict:
    try:
        result = await get_detail_pembayaran_member_repository(db_milkyverse, compid, id_batch)

        if not result:
            return {
                "status": False,
                "message": "Data tidak ditemukan"
            }
        
        return {
            "status": True,
            "message": "OK",
            "total_data": len(result["data"]),
            "total_nominal": result["total_nominal"],
            "data": result["data"]
        }
    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }