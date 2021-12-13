from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

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
