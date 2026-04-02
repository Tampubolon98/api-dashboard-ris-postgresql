from sqlalchemy import Column, String, Boolean, DateTime, Float, ForeignKey, Numeric, Integer
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship

class TaxMasukanModel(Base):
    __tablename__ = "taxentry"
    __table_args__ = {'schema': 'public'}
    
    kode = Column(String, primary_key=True)
    faktur_rmy = Column(String, primary_key=True)
    supplier_code = Column(String, primary_key=True)
    status_ap = Column(String)
    dpp = Column(Numeric(15, 2), nullable=True)
    ppn = Column(Numeric(15, 2), nullable=True)
    no_seri = Column(String)
    npwp = Column(String)
    RELEASE = Column(Integer)
    pay_date   = Column(TIMESTAMP(timezone=True), nullable=True)
    tgl_faktur = Column(TIMESTAMP(timezone=True), nullable=True)
    tax_date   = Column(TIMESTAMP(timezone=True), nullable=True)
    user_create = Column(String)
    date_create = Column(TIMESTAMP(timezone=True), server_default=func.now())
    user_modified = Column(String)
    date_modified = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    supplier_code = Column(String, ForeignKey("public.supplier.supplier_code"))

    suppliers = relationship("SupplierModel", back_populates="tax")

    def __repr__(self):
        return f"<TaxMasukanModel(kode={self.kode})>"