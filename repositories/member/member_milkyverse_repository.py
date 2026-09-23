from models.member.member_milkyverse_model import MasterPCA, MasterPD, MasterPY, MasterReceivh, MemberMilkyverseModel
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import cast, String, desc, asc
from models.serverside_model import ComponentServerSide

async def get_pembayaran_member_repository(db_milkyverse: AsyncSession, db: AsyncSession, compid: ComponentServerSide):
    print("cek1", compid.sort_type)
    order_by = 'created_date'
    if compid.sort_by:
        order_by = compid.sort_by

    query = (select(MemberMilkyverseModel.trx_pdf, MemberMilkyverseModel.created_date, MasterPCA.pca_amount, MasterPCA.pca_date_create, MasterReceivh.po_no)
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

    query_py = (select(MasterPY.pyh_id_batch, MasterPY.pyh_tgl_bayar, MasterPY.pyh_amount, MasterPY.pyh_status, MasterPD.pyd_no_po, MasterPD.pyd_no_invoice, MasterPD.pyd_no_rcv, MasterPD.pyd_nilai)
    .join(MasterPD, MasterPY.pyh_id_batch == MasterPD.pyd_id_batch))

    query_py = query_py.limit(compid.limit).offset(compid.skip)
    payment = await db.execute(query_py)
    result_payment = payment.all()
    

    mapping_data = {}
    for result in result_payment:
        mapping_data[result.pyh_id_batch] = {
            "id_batch": result.pyh_id_batch,
            "tgl_bayar": result.pyh_tgl_bayar,
            "amount": result.pyh_amount,
            "po_no": result.pyd_no_po,
            "rcv_no": result.pyd_no_rcv
        }

    data = []
    for item in result_member:
        list_data = mapping_data.get(item.po_no)

        data.append({
            "id_kasbon": item.trx_pdf,
            "nominal_transfer": item.pca_amount,
            "tanggal_transfer": item.pca_date_create,
            "id_batch": (
                list_data["id_batch"]
                if list_data
                else None
            ),
            "status": (
                list_data["status"]
                if list_data
                else None
            ),
            "po_no": (
                list_data["po_no"]
                if list_data
                else item.po_no
            ),
            "invoice_no": (
                list_data["invoice_no"]
                if list_data
                else None
            ),
            "rcv_no": (
                list_data["rcv_no"]
                if list_data
                else None
            ),
        })

    return data
