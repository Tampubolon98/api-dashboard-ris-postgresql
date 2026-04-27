from sqlalchemy import Column, String
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship

class SupplierModel(Base):
    __tablename__ = "supplier"
    __table_args__ = {"schema": "public"}

    supplier_code = Column(String, primary_key=True)
    supplier_name = Column(String)
    pkp_nonpkp = Column(String)

    tax = relationship("TaxMasukanModel", back_populates="suppliers")

    tax_keluaran = relationship("TaxKeluaranModel", back_populates="supplier")

    def __repr__(self):
        return f"<SupplierModel (supplier_code={self.supplier_code})>"