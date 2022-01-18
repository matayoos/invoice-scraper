from typing import Any

from sqlalchemy.orm import Session

from app.models.type_store import TypeStore
from app.schemas.type_store import TypeStoreCreate


def read_type_stores(db: Session, skip: int = 0, limit: int = 100) -> Any:
    return db.query(TypeStore).offset(skip).limit(limit).all()


def create_type_store(db: Session, obj_in: TypeStoreCreate) -> TypeStore:
    db_obj = TypeStore(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_type_store_by_id(db: Session, type_store_id: int) -> TypeStore:
    return db.query(TypeStore).get(type_store_id)
