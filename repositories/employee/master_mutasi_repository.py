from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.employee.master_mutasi_model import MasterMutasiModel

async def get_master_mutasi_repository(db: AsyncSession):
    result = await db.execute(
        select(MasterMutasiModel)
        .where(MasterMutasiModel.tanggal_keluar.is_(None))
    )

    data = result.scalars().all()
    return data