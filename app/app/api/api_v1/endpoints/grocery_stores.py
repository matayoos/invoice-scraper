from typing import List
from app.schemas.grocery_store import GroceryStore, GroceryStoreBase
from app.scraper.scraper_grocery_store import get_grocery_store_info

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.scraper.base import get_content

router = APIRouter()


@router.get("/", response_model=List[schemas.GroceryStore])
async def read_grocery_stores(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    return crud.get_grocery_stores(db=db, skip=skip, limit=limit)


@router.post("/")
async def create_grocery_stores(
    grocerystore: schemas.GroceryStoreCreate, db: Session = Depends(deps.get_db)
):
    return crud.create_grocery_store(db, grocerystore)


@router.get("/scrape", response_model=GroceryStoreBase)
async def scrappe_grocery_store(url: str):
    content = get_content(url)
    return get_grocery_store_info(content)
