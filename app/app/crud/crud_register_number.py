from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import and_

from app.models.register_number import RegisterNumber
from app.schemas.register_number import RegisterNumberCreate


def create_register_number(db: Session, obj_in: RegisterNumberCreate) -> RegisterNumber:
    db_obj = (
        db.query(RegisterNumber)
        .filter(
            and_(
                RegisterNumber.cnpj.like(obj_in.cnpj),
                RegisterNumber.inscricao_estadual.like(obj_in.inscricao_estadual),
            )
        )
        .first()
    )

    if db_obj:
        return db_obj
    else:
        db_obj = RegisterNumber(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
