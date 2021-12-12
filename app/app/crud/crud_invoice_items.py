from typing import List

from sqlalchemy.orm import Session

from app.models.invoice_items import InvoiceItems
from app.schemas.invoice_items import InvoiceItemsCreate


def get_invoice_items(
    db: Session, skip: int = 0, limit: int = 100
) -> List[InvoiceItems]:
    return db.query(InvoiceItems).offset(skip).limit(limit).all()


def create_invoice_items(
    db: Session, obj_in: InvoiceItemsCreate, invoice_id: int, item_id: int
) -> InvoiceItems:
    db_obj = InvoiceItems(**obj_in.dict(), invoice_id=invoice_id, item_id=item_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
