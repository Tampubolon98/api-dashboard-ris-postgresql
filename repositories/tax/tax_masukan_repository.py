from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.tax.tax_masukan_model import TaxMasukanModel
from models.supplier.supplier_model import SupplierModel
from schemas.tax.tax_masukan_schema import UpdateTax, TaxCreate, TaxNonapCreate
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date

async def get_tax_bahan_repository(db: AsyncSession, start_date: date, end_date: date):
    tax = await db.execute(select(TaxMasukanModel, SupplierModel).join(SupplierModel, TaxMasukanModel.supplier_code == SupplierModel.supplier_code).where(TaxMasukanModel.kode == 'B', TaxMasukanModel.pay_date.between(start_date, end_date)).order_by(TaxMasukanModel.supplier_code.asc()))

    data = tax.all()

    result = []
    for tax, suppliers in data:
        result.append({
            'kode': tax.kode,
            'supplier_code': tax.supplier_code,
            'supplier_name': suppliers.supplier_name,
            'status_ap': tax.status_ap,
            'faktur_rmy': tax.faktur_rmy,
            'dpp': tax.dpp,
            'ppn': tax.ppn,
            'no_seri': tax.no_seri,
            'npwp': tax.npwp,
            'RELEASE': tax.RELEASE,
            'pay_date': tax.pay_date,
            'tgl_faktur': tax.tgl_faktur,
            'tax_date': tax.tax_date,
            'user_create': tax.user_create,
            'date_create': tax.date_create,
            'user_modified': tax.user_modified,
            'date_modified': tax.date_modified
        })
    return result

async def update_tax_bahan_repository(faktur_rmy: str, updated_tax: TaxCreate, db: AsyncSession):
    result = await db.execute(
        select(TaxMasukanModel)
        .where(TaxMasukanModel.faktur_rmy == faktur_rmy)
    )

    tax = result.scalar()

    if tax is None:
        raise HTTPException(
            status_code=404,
            detail=f"tax bahan with faktur rmy {faktur_rmy} not found"
        )

    for key, value in updated_tax.dict(exclude_unset=True).items():
        setattr(tax, key, value)

    await db.commit()
    await db.refresh(tax)
    return tax

async def get_tax_nonap_repository(db: AsyncSession, start_date: date, end_date: date):
    tax = await db.execute(select(TaxMasukanModel, SupplierModel).join(SupplierModel, TaxMasukanModel.supplier_code == SupplierModel.supplier_code).where(TaxMasukanModel.kode == 'N', TaxMasukanModel.date_create.between(start_date, end_date)).order_by(TaxMasukanModel.date_create.desc()))

    data = tax.all()

    result = []
    for tax, suppliers in data:
        result.append({
            'kode': tax.kode,
            'supplier_code': tax.supplier_code,
            'supplier_name': suppliers.supplier_name,
            'status_ap': tax.status_ap,
            'faktur_rmy': tax.faktur_rmy,
            'dpp': tax.dpp,
            'ppn': tax.ppn,
            'no_seri': tax.no_seri,
            'npwp': tax.npwp,
            'RELEASE': tax.RELEASE,
            'pay_date': tax.pay_date,
            'tgl_faktur': tax.tgl_faktur,
            'tax_date': tax.tax_date,
            'user_create': tax.user_create,
            'date_create': tax.date_create,
            'user_modified': tax.user_modified,
            'date_modified': tax.date_modified
        })
    return result

async def create_tax_nonap_repository(create_tax: TaxNonapCreate, db: AsyncSession):
    new_post = TaxMasukanModel(**create_tax.model_dump())

    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post

async def update_tax_nonap_repository(faktur_rmy: str, update_tax: TaxNonapCreate, db: AsyncSession):
    result = await db.execute(select(TaxMasukanModel).where(TaxMasukanModel.faktur_rmy == faktur_rmy))
    
    tax = result.scalar()

    if tax is None:
        raise HTTPException(
            status_code=404,
            detail=f"tax non a/p with faktur rmy {faktur_rmy} not found"
        )
    
    for key, value in update_tax.dict(exclude_unset=True).items():
        setattr(tax, key, value)

    await db.commit()
    await db.refresh(tax)
    return tax