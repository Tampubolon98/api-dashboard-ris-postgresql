from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class MasterMutasiModel(Base):
    __tablename__ = "mutasi_emp"
    __table_args__ = {"schema": "public"}

    id_employee = Column(String, primary_key=True)
    nama = Column(String)
    tanggal_masuk = Column(TIMESTAMP(timezone=True), server_default=func.now())
    tanggal_keluar = Column(TIMESTAMP(timezone=True), server_default=func.now())
    kategori_karyawan = Column(String)
    kode_toko = Column(String)
    md_emp = Column(String)
    brand_emp = Column(String)
    supplier = Column(String)
    no_kk = Column(String)
    no_ktp = Column(String)
    nama_toko = Column(String)
    user_create = Column(String)
    date_create = Column(TIMESTAMP(timezone=True), server_default=func.now())
    user_updated = Column(String)
    date_updated = Column(TIMESTAMP(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<MasterMutasiModel (id_employee={self.id_employee})>"