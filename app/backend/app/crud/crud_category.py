from typing import Any

from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate


def read_categories(db: Session, skip: int = 0, limit: int = 100) -> Any:
    return db.query(Category).offset(skip).limit(limit).all()


def create_category(db: Session, obj_in: CategoryCreate) -> Category:
    db_obj = Category(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_category_by_id(db: Session, category_id: int) -> Category:
    return db.query(Category).get(category_id)


def get_category_by_name(db: Session, category_name: str) -> Category:
    return db.query(Category).filter(Category.name == category_name).first()
