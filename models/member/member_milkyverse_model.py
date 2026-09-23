from sqlalchemy import Column, String, DateTime, DECIMAL, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class MemberMilkyverseModel(Base):
    __tablename__ = "invmatching"
    __table_args__ = {"schema": "mkv"}

    trx_pdf = Column(String, primary_key=True)
    po_no = Column(String)
    flag = Column(String)
    flag_pdf = Column(Numeric)
    created_date = Column(DateTime)

    def __repr__(self):
        return f"<MemberMilkyverseModel (trx_pdf={self.trx_pdf})>"
    
class MasterPCA(Base):
    __tablename__ = "petty_cash_advance"
    __table_args__ = {"schema": "report"}

    pca_no_po = Column(String, primary_key=True)
    pca_amount = Column(String)
    pca_date_create = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<MasterPCA >"

class MasterReceivh(Base):
    __tablename__ = "drm_receivh"
    __table_args__ = {"schema": "mkv"}

    po_no = Column(String, primary_key=True)
    store_code = Column(String)
    rcv_no = Column(String)
    rcv_date = Column(DateTime, nullable=True)

class MasterPY(Base):
    __tablename__ = "payment_header"
    __table_args__ = {"schema": "idcash"}

    pyh_id_batch = Column(String, primary_key=True)
    pyh_tgl_bayar = Column(DateTime, nullable=True)
    pyh_amount = Column(String)
    pyh_status = Column(String)

class MasterPD(Base):
    __tablename__ = "payment_details"
    __table_args__ = {"schema": "idcash"}

    pyd_no_po = Column(String, primary_key=True)
    pyd_no_rcv = Column(String)
    pyd_no_invoice = Column(String)
    pyd_nilai = Column(String)
    pyd_id_batch = Column(String)