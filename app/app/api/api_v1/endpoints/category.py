from typing import Any, List
from app.schemas.category import CategoryResponse

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get(
    "/", response_model=List[schemas.CategoryResponse], status_code=status.HTTP_200_OK
)
def read_categories(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    return crud.read_categories(db, skip=skip, limit=limit)


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def create_category(
    obj_in: schemas.CategoryCreate, db: Session = Depends(deps.get_db)
) -> Any:
    is_a_registered_category = crud.get_category_by_name(db, obj_in.name)

    if is_a_registered_category:
        raise HTTPException(status_code=400, detail="Category already registered")

    return crud.create_category(db, obj_in=obj_in)
