from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

class MasterBrandBase(BaseModel):
    md: Optional[str] = None
    detail_brand: Optional[str] = None
    nama_supplier: Optional[str] = None
    user_create: Optional[str] = None
    date_create: Optional[datetime] = None

class AddMasterBrand(MasterBrandBase):
    pass

class MasterBrand(MasterBrandBase):
    id_brand_emp: Optional[str] = None

class MasterBrandResponse(BaseModel):
    status: bool
    message: str
    total_data: int
    data: list[MasterBrand]

class MasterSupplierResponse(BaseModel):
    status: bool
    message: str
    total_data: int
    data: List[str]