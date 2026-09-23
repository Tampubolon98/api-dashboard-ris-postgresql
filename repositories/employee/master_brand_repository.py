from models.employee.master_brand_model import MasterBrandModel
# from sqlalchemy.future import select, distinct
from sqlalchemy import select, distinct, desc
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.employee.master_brand_schema import AddMasterBrand
from models.employee.master_brand_model import MasterBrandModel

async def get_master_brand_repository(db: AsyncSession):
    result = await db.execute(select(MasterBrandModel).order_by(
        MasterBrandModel.id_brand_emp.desc()
    ))

    data = result.scalars().all()
    return data

async def create_master_brand_repository(create_brand: AddMasterBrand, db: AsyncSession):
    new_data = MasterBrandModel(**create_brand.model_dump())

    db.add(new_data)
    await db.commit()
    await db.refresh(new_data)
    return new_data

async def get_master_supplier_repository(db: AsyncSession):
    result = await db.execute(
        select(distinct(MasterBrandModel.nama_supplier))
        .order_by(MasterBrandModel.nama_supplier.asc())
    )

    data = result.scalars().all()
    return data

async def get_last_data_brand_repository(db: AsyncSession, prefix: str):
    print("cek1", prefix)
    result = await db.execute(select(MasterBrandModel).where(MasterBrandModel.id_brand_emp.like(f"{prefix}%"))).order_by(desc(MasterBrandModel.id_brand_emp))

    return result.scalars().first()