from fastapi import APIRouter, Depends
from typing import List
from controllers.member.member_milkyverse_controller import get_pembayaran_member_controller
from app.database import get_db_milkyverse, get_db
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.member.member_milkyverse_schema import MemberResponse
from models.serverside_model import ComponentServerSide

router = APIRouter()

@router.get("/member/get-pembayaran", response_model=MemberResponse)
async def get_pembayaran_member(db_milkyverse: AsyncSession = Depends(get_db_milkyverse), db: AsyncSession = Depends(get_db), comp: ComponentServerSide = Depends()):
    result = await get_pembayaran_member_controller(db_milkyverse, db, comp)
    return result