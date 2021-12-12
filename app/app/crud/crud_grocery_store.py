from typing import List

from sqlalchemy.orm import Session

from app.models.grocery_store import GroceryStore
from app.schemas.grocery_store import GroceryStoreCreate


def get_grocery_stores(
    db: Session, skip: int = 0, limit: int = 100
) -> List[GroceryStore]:
    return db.query(GroceryStore).offset(skip).limit(limit).all()


def create_grocery_store(db: Session, obj_in: GroceryStoreCreate) -> GroceryStore:
    db_obj = GroceryStore(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_grocery_store_by_id(db: Session, id: int) -> GroceryStore:
    return db.query(GroceryStore).filter(GroceryStore.id == id).first()
