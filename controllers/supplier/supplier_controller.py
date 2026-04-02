from repositories.supplier.supplier_repository import get_supplier_repository
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date

async def get_supplier_controller(db: AsyncSession, limit: int = 10):
    try:
        data = await get_supplier_repository(db, limit)

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