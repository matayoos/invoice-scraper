from typing import List

from sqlalchemy.orm import Session

from app.models.invoice_item import InvoiceItem
from app.schemas.invoice_item import InvoiceItemCreate
from app.models.item import Item


def get_invoice_items(
    db: Session, skip: int = 0, limit: int = 100
) -> List[InvoiceItem]:
    return db.query(InvoiceItem).offset(skip).limit(limit).all()


def create_invoice_item(
    db: Session, obj_in: InvoiceItemCreate, invoice_id: int, item_id: int
) -> InvoiceItem:
    db_obj = InvoiceItem(**obj_in.dict(), invoice_id=invoice_id, item_id=item_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_invoice_items_by_invoice_id(
    db: Session, grocery_store_id: int, skip: int = 0, limit: int = 100
):
    return (
        db.query(Item, InvoiceItem)
        .filter(InvoiceItem.grocery_store_id == grocery_store_id)
        .filter(Item.id == InvoiceItem.item_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
