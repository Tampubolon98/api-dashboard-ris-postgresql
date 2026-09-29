from services.member.member_milkyverse_service import get_pembayaran_members_service
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.member.member_milkyverse_schema import paramMember

async def get_pembayaran_member_controller(db_milkyverse: AsyncSession, db: AsyncSession, comp, params: paramMember):
    try:
        data = await get_pembayaran_members_service(db_milkyverse, db, comp, params)
        return data
    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }