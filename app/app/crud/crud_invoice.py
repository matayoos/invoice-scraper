from typing import List

from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate


def get_invoices(db: Session, skip: int = 0, limit: int = 100) -> List[Invoice]:
    return db.query(Invoice).offset(skip).limit.all()


def create_invoice(
    db: Session, obj_in: InvoiceCreate, grocery_store_id: int
) -> Invoice:
    db_obj = Invoice(**obj_in.dict(), grocery_store_id=grocery_store_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_invoices_by_grocery_store_id(
    db: Session, grocery_store_id: int, skip: int = 0, limit: int = 100
) -> List[Invoice]:
    return (
        db.query(Invoice)
        .filter(Invoice.grocery_store_id == grocery_store_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
