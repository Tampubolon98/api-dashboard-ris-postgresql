from models.member.member_milkyverse_model import MasterPCA, MasterPD, MasterPY, MasterReceivh, MemberMilkyverseModel
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import cast, String, desc, asc
from models.serverside_model import ComponentServerSide

async def get_pembayaran_member_repository(db_milkyverse: AsyncSession, db: AsyncSession, compid: ComponentServerSide):
    order_by = 'created_date'
    if compid.sort_by:
        order_by = compid.sort_by

    query = (select(MemberMilkyverseModel.trx_pdf.label("id_kasbon"), MasterPCA.pca_amount.label("nominal_transfer"), MasterPCA.pca_date_create.label("tanggal_transfer"))
    .join(MasterPCA, cast(MemberMilkyverseModel.po_no, String) == cast(MasterPCA.pca_no_po, String))
    .join(MasterReceivh, cast(MemberMilkyverseModel.po_no, String) == cast(MasterReceivh.po_no, String))
    .where(MemberMilkyverseModel.flag == '1', MemberMilkyverseModel.flag_pdf == 1))

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
