from sqlalchemy.orm.session import Session

from app import crud, schemas


def insert_grocery_store_info(db: Session, obj_in: list) -> int:
    register_number_id = crud.create_register_number(
        db, obj_in=schemas.RegisterNumberCreate(**obj_in)
    )

    grocery_store_id = crud.create_grocery_store(
        db,
        obj_in=schemas.GroceryStoreCreate(**obj_in),
        register_number_id=register_number_id,
    )

    return grocery_store_id


def insert_invoice_info(db: Session, obj_in: list, grocery_store_id: int) -> int:
    invoice_series_id = crud.create_invoice_series(
        db, obj_in=schemas.InvoiceSeriesCreate(**obj_in)
    )

    invoice_id = crud.create_invoice(
        db,
        obj_in=schemas.InvoiceCreate(**obj_in),
        grocery_store_id=grocery_store_id,
        invoice_series_id=invoice_series_id,
    )

    return invoice_id


def insert_invoice_items(
    db: Session, items: list, grocery_store_id: int, invoice_id: int
):
    for item in items:
        item_id = crud.create_item(
            db,
            obj_in=schemas.ItemCreate(**item),
            grocery_store_id=grocery_store_id,
        )

        unit_id = crud.create_unit(db, obj_in=schemas.UnitCreate(name=item["unit"]))

        item_details_id = crud.create_item_details(
            db,
            obj_in=schemas.ItemDetailsCreate(**item),
            item_id=item_id,
            unit_id=unit_id,
        )

        crud.create_invoice_item(
            db,
            obj_in=schemas.InvoiceItemCreate(**item),
            invoice_id=invoice_id,
            item_details_id=item_details_id,
        )
