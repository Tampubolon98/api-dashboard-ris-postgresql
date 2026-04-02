from fastapi import HTTPException
from models.supplier.supplier_model import SupplierModel
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date

async def get_supplier_repository(db: AsyncSession, limit: int = 10):
    suppliers = await db.execute(select(SupplierModel).distinct().limit(limit))
    data = suppliers.scalars().all()
    return data