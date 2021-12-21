from typing import List

from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.item import ItemCreate


def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    return db.query(Item).offset(skip).limit(limit).all()


def create_item(db: Session, obj_in: ItemCreate, grocery_store_id: int) -> int:
    db_obj = db.query(Item).filter(Item.item_id.like(obj_in.item_id)).first()

    if db_obj:
        return db_obj.id
    else:
        db_obj = Item(**obj_in.dict(), grocery_store_id=grocery_store_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj.id
