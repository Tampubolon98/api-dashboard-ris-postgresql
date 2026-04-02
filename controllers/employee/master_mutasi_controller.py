from repositories.employee.master_mutasi_repository import get_master_mutasi_repository
from sqlalchemy.ext.asyncio import AsyncSession

async def get_master_mutasi_controller(db: AsyncSession):
    try:
        data = await get_master_mutasi_repository(db)

        return {
            "status": True,
            "message": 'OK',
            "total_data": len(data),
            "data": data
        }
    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }