from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from controllers.member.member_milkyverse_controller import get_pembayaran_member_controller, get_detail_pembayaran_controller
from app.database import get_db_milkyverse, get_db
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.member.member_milkyverse_schema import MemberResponse
from models.serverside_model import ComponentServerSide
from datetime import date, datetime

router = APIRouter()

@router.get("/member/get-pembayaran", response_model=MemberResponse)
async def get_pembayaran_member(id_batch: Optional[str] = None, status: Optional[str] = None, start_date: Optional[date] = None, end_date: Optional[date] = None, db_milkyverse: AsyncSession = Depends(get_db_milkyverse), db: AsyncSession = Depends(get_db), comp: ComponentServerSide = Depends()):
    result = await get_pembayaran_member_controller(db_milkyverse, db, comp, id_batch, status, start_date, end_date)
    return result

@router.get("/member/get-detail-pembayaran", response_model=MemberResponse)
async def get_detail_pembayaran_member(id_batch: str, db_milkyverse: AsyncSession = Depends(get_db_milkyverse), comp: ComponentServerSide = Depends()):
    result = await get_detail_pembayaran_controller(db_milkyverse, comp, id_batch)
    return result