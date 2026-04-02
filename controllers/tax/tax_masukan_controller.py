from repositories.tax.tax_masukan_repository import get_tax_bahan_repository, update_tax_bahan_repository, get_tax_nonap_repository, create_tax_nonap_repository, update_tax_nonap_repository
from schemas.tax.tax_masukan_schema import TaxCreate, TaxNonapCreate
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, date

async def get_tax_bahan_controller(db: AsyncSession, start_date: date, end_date: date):
    try:
        data = await get_tax_bahan_repository(db, start_date, end_date)

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
    
async def update_tax_bahan_controller(db: AsyncSession, faktur_rmy: str, update_tax: TaxCreate):
    try:
        data = await update_tax_bahan_repository(faktur_rmy=faktur_rmy, updated_tax=update_tax, db=db)

        return {
            "status": True,
            "message": "Data berhasil diperbarui",
            "data": data
        }
    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }
    
async def get_tax_nonap_controller(db: AsyncSession, start_date: date, end_date: date):
    try:
        data = await get_tax_nonap_repository(db, start_date, end_date)

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
    
async def create_tax_nonap_controller(db: AsyncSession, create_tax: TaxNonapCreate):
    try:
        data = await create_tax_nonap_repository(create_tax=create_tax, db=db)

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
    
async def update_tax_nonap_controller(db: AsyncSession, faktur_rmy: str, update_tax: TaxNonapCreate):
    try:
        data = await update_tax_nonap_repository(faktur_rmy=faktur_rmy, update_tax=update_tax, db=db)

        return {
            "status": True,
            "message": "Data berhasil diperbarui",
            "data": data
        }
    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }