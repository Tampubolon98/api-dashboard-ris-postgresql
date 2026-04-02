from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from decimal import Decimal

class TaxBase(BaseModel):
    kode: str
    supplier_code: str
    supplier_name: str
    status_ap: str
    faktur_rmy: str
    dpp: Optional[Decimal] = None
    ppn: Optional[Decimal] = None
    no_seri: str
    npwp: str
    RELEASE: Optional[Decimal] = None
    pay_date: Optional[datetime] = None
    tgl_faktur: Optional[datetime] = None
    tax_date: Optional[datetime] = None
    user_create: str
    date_create: Optional[datetime] = None
    user_modified: str
    date_modified: Optional[datetime] = None

    class Config:
        orm_mode = True

class TaxResponse(BaseModel):
    status: bool
    message: str
    total_data: int
    data: list[TaxBase]

class UpdateTaxBase(BaseModel):
    no_seri: str
    tax_date: Optional[datetime] = None
    ppn: Optional[Decimal] = None
    npwp: str
    RELEASE: Optional[Decimal] = None
    user_modified: str = "SYSTEM"
    date_modified: Optional[datetime] = None

class TaxCreate(UpdateTaxBase):
    pass

class UpdateTax(UpdateTaxBase):
    faktur_rmy: str

    class Config:
        orm_mode = True

class TaxNonapBase(BaseModel):
    kode: str
    supplier_code: str
    faktur_rmy: str
    no_seri: str
    tax_date: Optional[datetime] = None
    tgl_faktur: Optional[datetime] = None
    pay_date: Optional[datetime] = None
    dpp: Optional[Decimal] = None
    ppn: Optional[Decimal] = None
    npwp: str
    RELEASE: Optional[Decimal] = None
    user_create: str = "SYSTEM"
    date_create: Optional[datetime] = None
    user_modified: str = 'SYSTEM'
    date_modified: Optional[datetime] = None

class TaxNonapCreate(TaxNonapBase):
    pass

    class Config:
        from_attributes = True

class UpdateTaxNonap(TaxNonapBase):
    faktur_rmu: str

    class Config:
        orm_mode = True

class CreateTaxResponse(BaseModel):
    status: bool
    message: str

class UpdateTaxResponse(BaseModel):
    status: bool
    message: str

