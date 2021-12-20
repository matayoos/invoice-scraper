from sqlalchemy.orm import Session

from app.models.invoice_series import InvoiceSeries
from app.schemas.invoice_series import InvoiceSeriesCreate


def create_invoice_series(db: Session, obj_in: InvoiceSeriesCreate) -> InvoiceSeries:
    db_obj = (
        db.query(InvoiceSeries)
        .filter(InvoiceSeries.series_number.like(obj_in.series_number))
        .first()
    )

    if db_obj:
        return db_obj
    else:
        db_obj = InvoiceSeries(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
