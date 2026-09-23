# from sqlalchemy import Column, String, DateTime, Date
# from sqlalchemy.dialects.postgresql import TIMESTAMP
# from sqlalchemy.sql import func
# from app.database import Base

# class MasterStoreModel(Base):
#     __tablename__ = "p_c_x_homebase_tbl"
#     __table_args__ = {"schema": "public"}

#     employee_id = Column(String)
#     homebase = Column(String)
#     company_id = Column(String)
#     valid_from = Column(Date)
#     valid_to = Column(Date)

# def __repr__(self):
#     return f"<MasterStoreModel (employee_id={self.employee_id})>"