from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate


def create_category(db: Session, obj_in: CategoryCreate) -> Category:
    db_obj = db.query(Category).filter(Category.name.like(obj_in.name))

    if db_obj:
        return db_obj
    else:
        db_obj = Category(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
