from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional
from decimal import Decimal

class MemberMilkyverseBase(BaseModel):
    id_kasbon: Optional[str] = None
    nominal_transfer: Optional[Decimal] = None
    tanggal_transfer: Optional[datetime] = None
    id_batch: Optional[str] = None
    status: Optional[str] = None
    po_no: Optional[str] = None
    invoice_no: Optional[str] = None
    rcv_no: Optional[str] = None
    create_by: Optional[str] = None
    create_date: Optional[datetime] = None

class MemberResponse(BaseModel):
    status: bool
    message: str
    total_data: Optional[int] = None
    data: Optional[list[MemberMilkyverseBase]] = None

class MemberDetailResponse(BaseModel):
    status: bool
    message: str
    total_data: Optional[int] = None
    total_nominal: Optional[Decimal] = None
    data: Optional[list[MemberMilkyverseBase]] = None