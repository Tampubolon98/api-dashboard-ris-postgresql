from repositories.tax.tax_keluaran_repository import get_tax_keluaran_repository, create_tax_keluaran_repository
from schemas.tax.tax_keluaran_schema import TaxKeluaranCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def get_tax_keluaran_controller(db: AsyncSession, limit: int = 10):
    try:
        data = await get_tax_keluaran_repository(db, limit)

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
    
async def create_tax_keluaran_controller(db: AsyncSession, create_tax: TaxKeluaranCreate):
    try:
        data = await create_tax_keluaran_repository(create_tax=create_tax, db=db)
        
        return {
            "status": True,
            "message": "Data berhasil ditambahkan",
            "data": data
        }
    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }