from sqlalchemy.orm import Session

from app.models.unit import Unit
from app.schemas.unit import UnitCreate


def create_unit(db: Session, obj_in: UnitCreate) -> Unit:
    db_obj = db.query(Unit).filter(Unit.name.like(obj_in.name)).first()

    if db_obj:
        return db_obj
    else:
        db_obj = Unit(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
