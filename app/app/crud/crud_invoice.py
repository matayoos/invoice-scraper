from typing import List

from sqlalchemy import extract
from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate
from sqlalchemy.sql.elements import and_


def get_invoices(db: Session, skip: int = 0, limit: int = 100) -> List[Invoice]:
    return db.query(Invoice).offset(skip).limit(limit).all()


def create_invoice(
    db: Session, obj_in: InvoiceCreate, grocery_store_id: int, invoice_series_id: int
) -> Invoice:
    db_obj = db.query(Invoice).filter(Invoice.url.like(obj_in.url)).first()

    if db_obj:
        return db_obj.id
    else:
        db_obj = Invoice(
            **obj_in.dict(),
            grocery_store_id=grocery_store_id,
            invoice_series_id=invoice_series_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj.id


def get_invoices_by_grocery_store_id(
    db: Session, grocery_store_id: int, limit: int = 100
) -> List[Invoice]:
    return (
        db.query(Invoice)
        .filter(Invoice.grocery_store_id == grocery_store_id)
        .limit(limit)
        .all()
    )


def get_invoice_by_url(db: Session, url: str) -> Invoice:
    return db.query(Invoice).filter(Invoice.url == url).first()


def get_invoice_by_id(db: Session, id: int) -> Invoice:
    return db.query(Invoice).get(id)


def get_invoice_by_year(
    db: Session, year: int, skip: int = 0, limit: int = 100
) -> List[Invoice]:
    return (
        db.query(Invoice)
        .filter(extract("year", Invoice.date_time) == year)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_invoice_by_year_and_month(
    db: Session, year: int, month: int, skip: int = 0, limit: int = 100
) -> List[Invoice]:
    return (
        db.query(Invoice)
        .filter(
            and_(
                extract("year", Invoice.date_time) == year,
                extract("month", Invoice.date_time) == month,
            )
        )
        .offset(skip)
        .limit(limit)
        .all()
    )
