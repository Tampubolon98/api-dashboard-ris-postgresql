# from services.employee.master_store_service import get_master_store_service
# from sqlalchemy.ext.asyncio import AsyncSession

# async def get_master_store_controller(db: AsyncSession, search_term: str, store_code: str):
#     try:
#         data = await get_master_store_service(db, search_term, store_code)

#         return data
#     except Exception as e:
#         return {
#             "status": False,
#             "message": str(e)
#         }