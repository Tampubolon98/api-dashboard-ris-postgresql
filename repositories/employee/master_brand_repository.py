from models.employee.master_brand_model import MasterBrandModel
# from sqlalchemy.future import select, distinct
from sqlalchemy import select, distinct
from sqlalchemy.ext.asyncio import AsyncSession

async def get_master_brand_repository(db: AsyncSession):
    result = await db.execute(select(MasterBrandModel).order_by(
        MasterBrandModel.id_brand_emp.desc()
    ))

    data = result.scalars().all()
    return data


async def get_master_supplier_repository(db: AsyncSession):
    result = await db.execute(
        select(distinct(MasterBrandModel.nama_supplier))
        .order_by(MasterBrandModel.nama_supplier.asc())
    )

    data = result.scalars().all()
    return data
