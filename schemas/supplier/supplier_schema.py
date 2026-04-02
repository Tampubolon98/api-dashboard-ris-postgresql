from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from decimal import Decimal

class SupplierBase(BaseModel):
    supplier_code: str
    supplier_name: str

    class Config:
        orm_mode = True

class SupplierResponse(BaseModel):
    status: bool
    message: str
    total_data: int
    data: list[SupplierBase]