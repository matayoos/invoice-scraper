from typing import List

from fastapi import APIRouter, Depends, status
from pydantic.main import BaseModel
from sqlalchemy.orm import Session

from app import crud, schemas, scraper
from app.api import deps

router = APIRouter()


class UrlList(BaseModel):
    url: List


@router.get("/", response_model=List[schemas.Invoice])
async def read_invoices(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    return crud.get_invoices(db=db, skip=skip, limit=limit)


@router.post("/", status_code=status.HTTP_200_OK)
def register_invoice(url: str, db: Session = Depends(deps.get_db)):
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
            item_details_id=x.id,
        )


@router.post("/invoice-list", status_code=status.HTTP_200_OK)
def register_invoice_list(invoice_list: UrlList, db: Session = Depends(deps.get_db)):
    i = 0
    index_erro = list()

    for url in invoice_list.url:

        i += 1

        is_a_registered_url = crud.get_invoice_by_url(db, url)

        if not is_a_registered_url:
            try:
                content = scraper.get_content(url)

                grocery_store_info = scraper.get_grocery_store_info(content)
                invoice_info = scraper.get_invoice_info(content, url)
                items = scraper.get_items(content)

                register_number_id = crud.create_register_number(
                    db, obj_in=schemas.RegisterNumberCreate(**grocery_store_info)
                )
                grocery_store_id = crud.create_grocery_store(
                    db,
                    obj_in=schemas.GroceryStoreCreate(**grocery_store_info),
                    register_number_id=register_number_id,
                )

                invoice_series_id = crud.create_invoice_series(
                    db, obj_in=schemas.InvoiceSeriesCreate(**invoice_info)
                )
                invoice_id = crud.create_invoice(
                    db,
                    obj_in=schemas.InvoiceCreate(**invoice_info),
                    grocery_store_id=grocery_store_id,
                    invoice_series_id=invoice_series_id,
                )

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
            except:
                index_erro.append(i)

    print(index_erro)
