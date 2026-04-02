from fastapi import APIRouter, Depends
from controllers.supplier.supplier_controller import get_supplier_controller
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
from schemas.supplier.supplier_schema import SupplierResponse

router = APIRouter()

@router.get("/supplier/get-supplier", response_model=SupplierResponse)
async def get_supplier(db: AsyncSession = Depends(get_db), limit: int = 10):
    result = await get_supplier_controller(db, limit)
    return result

