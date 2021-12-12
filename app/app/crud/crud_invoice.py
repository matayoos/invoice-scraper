from typing import List

from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate


def get_invoices(db: Session, skip: int = 0, limit: int = 100) -> List[Invoice]:
    return db.query(Invoice).offset(skip).limit.all()


def creater_invoice(db: Session, obj_in: InvoiceCreate, invoice_id: int) -> Invoice:
    db_obj = Invoice(**obj_in.dict(), invoice_id=invoice_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
