from typing import Any

from sqlalchemy.orm import Session

from app.models.category import Category
from app.models.type import Type
from app.schemas.type import TypeCreate


def read_type(db: Session, skip: int = 0, limit: int = 100) -> Any:
    return db.query(Type).offset(skip).limit(limit).all()


def create_type(db: Session, obj_in: TypeCreate) -> Category:
    db_obj = Type(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_type_by_id(db: Session, type_id: int) -> Type:
    return db.query(Type).get(type_id)


def get_type_by_name(db: Session, type_name: str) -> Type:
    return db.query(Type).filter(Type.name == type_name).first()
