from models.member.member_milkyverse_model import MasterPCA, MasterPD, MasterPY, MasterReceivh, MemberMilkyverseModel
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import cast, String, desc, asc, Date, func
from models.serverside_model import ComponentServerSide
from datetime import date, datetime
from typing import Optional

async def get_pembayaran_member_repository(db_milkyverse: AsyncSession, db: AsyncSession, compid: ComponentServerSide, id_batch: Optional[str] = None, status: Optional[str] = None, start_date: Optional[date] = None, end_date: Optional[date] = None) -> list:
    order_by = 'trx_pdf'
    if compid.sort_by:
        order_by = compid.sort_by

    query = (select(MemberMilkyverseModel.trx_pdf.label("id_kasbon"), func.sum(MasterPCA.pca_amount).label("nominal_transfer"), func.max(MasterPCA.pca_date_create).label("tanggal_transfer"), func.max(MemberMilkyverseModel.created_date).label("created_date"))
    .join(MasterPCA, cast(MemberMilkyverseModel.po_no, String) == cast(MasterPCA.pca_no_po, String))
    .join(MasterReceivh, cast(MemberMilkyverseModel.po_no, String) == cast(MasterReceivh.po_no, String))
    .where(MemberMilkyverseModel.flag == '1', MemberMilkyverseModel.flag_pdf == 1).group_by(MemberMilkyverseModel.trx_pdf))

    if id_batch:
        query = query.where(MemberMilkyverseModel.trx_pdf == id_batch)

    if start_date:
        query = query.where(cast(MasterPCA.pca_date_create, Date) >= start_date)

    if end_date:
        query = query.where(cast(MasterPCA.pca_date_create, Date) <= end_date)

    if compid.sort_type.lower() == "desc":
        query = query.order_by(desc(getattr(MemberMilkyverseModel, order_by)))
    else:
        query = query.order_by(getattr(MemberMilkyverseModel, order_by))
    
    query = query.limit(compid.limit).offset(compid.skip)
    member = await db_milkyverse.execute(query)
    result_member = member.all()

    id_kasbon_list = list({
        str(item.id_kasbon)
        for item in result_member
        if item.id_kasbon is not None
    })

    mapping_data = {}
    if id_kasbon_list:
        query_py = (
            select(
                MasterPY.pyh_id_batch,
                MasterPY.pyh_tgl_bayar,
                MasterPY.pyh_amount,
                MasterPY.pyh_status,
                MasterPY.pyh_create_by,
                MasterPY.pyh_create_date,
                MasterPD.pyd_no_po,
                MasterPD.pyd_no_invoice,
                MasterPD.pyd_no_rcv,
                MasterPD.pyd_nilai,
            )
            .join(
                MasterPD,
                MasterPY.pyh_id_batch == MasterPD.pyd_id_batch,
            )
            .where(
                cast(MasterPY.pyh_id_batch, String).in_(id_kasbon_list)
            )
        )

        if status:
            query_py = query_py.where(MasterPY.pyh_status == status.upper())

        payment_result = await db.execute(query_py)
        result_payment = payment_result.all()

        for result in result_payment:
            key = str(result.pyh_id_batch)

            mapping_data.setdefault(key, []).append({
                "id_batch": result.pyh_id_batch,
                "tanggal_bayar": result.pyh_tgl_bayar,
                "amount": result.pyh_amount,
                "status": result.pyh_status,
                "create_by": result.pyh_create_by,
                "create_date": result.pyh_create_date,
                "invoice_no": result.pyd_no_invoice,
                "rcv_no": result.pyd_no_rcv,
                "no_po": result.pyd_no_po,
                "nilai": result.pyd_nilai,
            })

    data = []
    for item in result_member:
        key = str(item.id_kasbon)
        list_data = mapping_data.get(key, [])
        payment = list_data[0] if list_data else {}

        data.append({
            "id_kasbon": item.id_kasbon,
            "nominal_transfer": item.nominal_transfer,
            "tanggal_transfer": item.tanggal_transfer,
            "id_batch": payment.get("id_batch"),
            "status": payment.get("status"),
            "invoice_no": payment.get("invoice_no"),
            "rcv_no": payment.get("rcv_no"),
            "create_by": payment.get("create_by"),
            "create_date": payment.get("create_date"),
            "payment_data": list_data,
        })

    return data

async def get_detail_pembayaran_member_repository(db_milkyverse: AsyncSession, compid: ComponentServerSide, id_batch: str) -> list:
    order_by = 'created_date'
    if compid.sort_by:
        order_by = compid.sort_by

    query = (select(MemberMilkyverseModel.po_no, MemberMilkyverseModel.rcv_no, MemberMilkyverseModel.date_pdf, MemberMilkyverseModel.flag_pdf, MemberMilkyverseModel.trx_pdf.label('id_kasbon'), MasterReceivh.invoice_no, MasterPCA.pca_no_po, MasterPCA.pca_amount.label('nominal_transfer'), MasterPCA.pca_date_create.label('tanggal_transfer'), MasterPCA.pca_user_create, MasterPCA.pca_pcr_code, MasterPCA.pca_payment_type, MasterPCA.pca_store_code, MasterPCA.pca_amount.label("nominal_transfer"))
    .join(MasterPCA, cast(MemberMilkyverseModel.po_no, String) == cast(MasterPCA.pca_no_po, String))
    .join(MasterReceivh, cast(MemberMilkyverseModel.po_no, String) == cast(MasterReceivh.po_no, String))
    .where(MemberMilkyverseModel.flag == '1', MemberMilkyverseModel.flag_pdf == 1, MemberMilkyverseModel.trx_pdf == id_batch))

    total_query = (
        select(
            func.coalesce(
                func.sum(MasterPCA.pca_amount),
                0
            )
        )
        .select_from(MemberMilkyverseModel)
        .join(
            MasterPCA,
            cast(MemberMilkyverseModel.po_no, String)
            == cast(MasterPCA.pca_no_po, String)
        )
        .join(
            MasterReceivh,
            cast(MemberMilkyverseModel.po_no, String)
            == cast(MasterReceivh.po_no, String)
        )
        .where(
            MemberMilkyverseModel.flag == "1",
            MemberMilkyverseModel.flag_pdf == 1,
            MemberMilkyverseModel.trx_pdf == id_batch
        )
    )

    if compid.sort_type.lower() == 'desc':
        query = query.order_by(desc(getattr(MemberMilkyverseModel, order_by)))
    else:
        query = query.order_by(getattr(MemberMilkyverseModel, order_by))

    total_result = await db_milkyverse.execute(total_query)
    total_nominal = total_result.scalar_one()

    query = query.limit(compid.limit).offset(compid.skip)
    member_detail = await db_milkyverse.execute(query)
    result_member_detail = member_detail.all()

    return {
        "data": result_member_detail,
        "total_nominal": total_nominal
    }
