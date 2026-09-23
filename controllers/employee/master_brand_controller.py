from repositories.employee.master_brand_repository import get_master_brand_repository, get_master_supplier_repository, create_master_brand_repository
from sqlalchemy.ext.asyncio import AsyncSession

async def get_master_brand_controller(db: AsyncSession):
    try:
        data = await get_master_brand_repository(db)

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
    
async def create_master_brand_controller(create_brand, db: AsyncSession):
    try:
        data = await create_master_brand_repository(create_brand=create_brand, db=db)

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
    
async def get_master_supplier_controller(db: AsyncSession):
    try:
        data = await get_master_supplier_repository(db)

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