from repositories.employee.master_brand_repository import create_master_brand_repository, get_last_data_brand_repository
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from schemas.employee.master_brand_schema import AddMasterBrand
from datetime import date, datetime
from sqlalchemy import select, desc

async def create_master_brand_service(create_brand: AddMasterBrand, db: AsyncSession):
    try:
        now = datetime.now()
        day = now.strftime("%d") 
        month = now.strftime("%m") 
        year = now.strftime("%Y")
        prefix = f"{year}{month}"
        print("data1", prefix)

        last_data = get_last_data_brand_repository(db, prefix)
        
        if last_data:
            last_number = int(last_data.id_brand_emp[-3:])
            new_number = last_number + 1
        else:
            new_number = 1

        id_brand = f"{prefix}{new_number:03d}"
        print('data2', id_brand)

        new_data = [
            ''
        ]

    except Exception as e:
        await db.rollback()
        raise e