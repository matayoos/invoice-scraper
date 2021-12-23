from typing import Any, List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, scraper
from app.api import deps

router = APIRouter()


@router.get(
    "/", response_model=List[schemas.InvoiceResponse], status_code=status.HTTP_200_OK
)
def read_invoices(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    return crud.get_invoices(db=db, skip=skip, limit=limit)


@router.post(
    "/", response_model=schemas.InvoiceResponse, status_code=status.HTTP_200_OK
)
def register_invoice(url: str, db: Session = Depends(deps.get_db)) -> Any:
    is_a_registered_url = crud.get_invoice_by_url(db, url)

    if is_a_registered_url:
        raise HTTPException(status_code=400, detail="Invoice already registered")

    try:
        return crud.register_invoice(db, url)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Error! Some problem happens during invoice registration, try again later",
        )


@router.post(
    "/list", response_model=schemas.UrlListResponse, status_code=status.HTTP_200_OK
)
def register_invoice_list(
    invoice_list: schemas.UrlList, db: Session = Depends(deps.get_db)
) -> Any:
    invoice_list_total = len(invoice_list.url)
    registered = 0
    errors = list()
    already_registered = list()

    for url in invoice_list.url:
        is_a_registered_url = crud.get_invoice_by_url(db, url)

        if not is_a_registered_url:
            try:
                crud.register_invoice(db, url)
                registered += 1
            except Exception:
                errors.append(url)
        else:
            already_registered.append(url)

    return {
        "invoice_list_total": invoice_list_total,
        "registered": registered,
        "already_registered": already_registered,
        "errors": errors,
    }


@router.get(
    "/{year}",
    response_model=List[schemas.InvoiceResponse],
    status_code=status.HTTP_200_OK,
)
def get_invoice_by_year(
    year: int, db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    return crud.get_invoice_by_year(db, year=year, skip=skip, limit=limit)


@router.get(
    "/{year}/{month}",
    response_model=List[schemas.InvoiceResponse],
    status_code=status.HTTP_200_OK,
)
def get_invoice_by_year_and_month(
    year: int,
    month: int,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return crud.get_invoice_by_year_and_month(
        db, year=year, month=month, skip=skip, limit=limit
    )
