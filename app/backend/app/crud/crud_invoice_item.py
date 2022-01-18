from typing import Any, List

from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import and_

from app.models.invoice_item import InvoiceItem
from app.schemas.invoice_item import InvoiceItemCreate, InvoiceItemResponse
from app.models.item_details import ItemDetails
from app.models.unit import Unit


def get_invoice_items(
    db: Session, skip: int = 0, limit: int = 100
) -> List[InvoiceItem]:
    return db.query(InvoiceItem).offset(skip).limit(limit).all()


def create_invoice_item(
    db: Session, obj_in: InvoiceItemCreate, invoice_id: int, item_details_id: int
) -> InvoiceItem:
    db_obj = InvoiceItem(
        **obj_in.dict(), invoice_id=invoice_id, item_details_id=item_details_id
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_invoice_items_by_invoice_id(
    db: Session, invoice_id: int, skip: int = 0, limit: int = 100
) -> List[InvoiceItemResponse]:
    return (
        db.query(
            InvoiceItem.id,
            ItemDetails.description,
            Unit.name,
            InvoiceItem.qty,
            InvoiceItem.value,
        )
        .select_from(ItemDetails)
        .join(Unit)
        .filter(
            and_(
                InvoiceItem.invoice_id == invoice_id,
                ItemDetails.id == InvoiceItem.item_details_id,
                Unit.id == ItemDetails.unit_id,
            )
        )
        .offset(skip)
        .limit(limit)
        .all()
    )
