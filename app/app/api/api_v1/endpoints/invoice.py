from typing import List
from app.scraper.scraper_invoice import get_invoice_info

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.schemas.invoice import InvoiceBase
from app.scraper.base import get_content, get_iframe_url

router = APIRouter()


@router.get("/", response_model=List[schemas.Invoice])
async def read_invoices(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    return crud.get_invoices(db=db, skip=skip, limit=limit)


@router.post("/", response_model=InvoiceBase)
async def register_invoice(url: str):
    content = get_content(url)
    iframe_url = get_iframe_url(url)
    return get_invoice_info(content, iframe_url)
