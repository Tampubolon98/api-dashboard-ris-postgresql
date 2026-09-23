from models.employee.master_store_model import MasterStoreModel
from sqlalchemy.future import select, func
from sqlalchemy.ext.asyncio import AsyncSession

async def get_master_store_repository(db: AsyncSession, search_term: str, store_code: str):
    store = func.split_part(
        MasterStoreModel.homebase,
        ' - ',
        1
    ).label("store")

    store_name = func.split_part(
        MasterStoreModel.homebase,
        ' - ',
        2
    ).label("store_name")

    query = select(store, store_name)

    if search_term:
        query = query.where(
            func.lower(MasterStoreModel.homebase).like(f"%{search_term.lower()}%"),
            func.upper(MasterStoreModel.homebase).like(f"%{search_term.upper()}%")
        )

    query = query.order_by(store.asc())
    result = await db.execute(query)
    return result.all()