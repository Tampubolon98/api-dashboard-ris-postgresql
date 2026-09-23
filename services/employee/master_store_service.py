# from repositories.employee.master_store_repository import get_master_store_repository
# from app.database import get_db
# from sqlalchemy.ext.asyncio import AsyncSession

# async def get_master_store_service(db: AsyncSession, search_term: str, store_code: str):
#     try:
#         if store_code == "" or store_code is None:
#             return { 
#                 "status": False,
#                 "message": "Store Code tidak valid"
#             }
        
#         result = await get_master_store_repository(db, search_term, store_code)

#         if not result:
#             return {
#                 "status": False,
#                 "message": "Data tidak ditemukan"
#             }
        
#         return {
#             "status": True,
#             "message": "OK",
#             "total_data": len(result),
#             "data": result
#         }
#     except Exception as e:
#         return {
#             "status": False,
#             "message": str(e)
#         }