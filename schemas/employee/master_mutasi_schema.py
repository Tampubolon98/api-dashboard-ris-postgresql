from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MasterMutasiBase(BaseModel):
    nama: Optional[str] = None
    tanggal_masuk: Optional[datetime] = None
    tanggal_keluar: Optional[datetime] = None
    kategori_karyawan: Optional[str] = None
    kode_toko: Optional[str] = None
    md_emp: Optional[str] = None
    brand_emp: Optional[str] = None
    supplier: Optional[str] = None
    no_kk: Optional[str] = None
    no_ktp: Optional[str] = None
    nama_toko: Optional[str] = None

class AddMasterMutasi(MasterMutasiBase):
    pass

class MasterMutasi(MasterMutasiBase):
    id_employee: Optional[str] = None

class MasterMutasiResponse(BaseModel):
    status: bool
    message: str
    total_data: int
    data: list[MasterMutasi]