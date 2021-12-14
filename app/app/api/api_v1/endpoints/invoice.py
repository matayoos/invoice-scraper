from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import crud, schemas, scraper
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Invoice])
async def read_invoices(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    return crud.get_invoices(db=db, skip=skip, limit=limit)


@router.post("/", status_code=status.HTTP_200_OK)
async def register_invoice(url: str, db: Session = Depends(deps.get_db)):
    content = scraper.get_content(url)
    iframe_url = scraper.get_iframe_url(url)

    grocery_info = scraper.get_grocery_store_info(content)
    invoice_info = scraper.get_invoice_info(content, iframe_url)
    items = scraper.get_items(content)

    grocery_store = crud.create_grocery_store(db, grocery_info)
    invoice = crud.create_invoice(
        db, obj_in=invoice_info, grocery_store_id=grocery_store.id
    )

    for item in items:
        x = crud.create_item(
            db, obj_in=schemas.ItemCreate(**item), grocery_store_id=grocery_store.id
        )

        crud.create_invoice_item(
            db,
            obj_in=schemas.InvoiceItemCreate(**item),
            invoice_id=invoice.id,
            item_id=x.id,
        )
