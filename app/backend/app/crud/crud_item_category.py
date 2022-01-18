from sqlalchemy.orm import Session, session

from app.models.item_category import ItemCategory
from app.schemas.item_category import ItemCategoryCreate


def create_item_category(db: Session, obj_in: ItemCategoryCreate) -> ItemCategory:
    db_obj = ItemCategory(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
