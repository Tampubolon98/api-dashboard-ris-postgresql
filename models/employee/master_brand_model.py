from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class MasterBrandModel(Base):
    __tablename__ = "master_brand_emp"
    __table_args__ = {"schema": "public"}

    md = Column(String)
    detail_brand = Column(String)
    nama_supplier = Column(String)
    id_brand_emp = Column(String, primary_key=True)
    user_create = Column(String)
    date_create = Column(TIMESTAMP(timezone=True), server_default=func.now())

def __repr__(self):
    return f"<MasterBrandModel (id_brand_emp={self.id_brand_emp})>"