from sqlalchemy.orm import Session

from app.models.item_detail import ItemDetail
from app.schemas.item_detail import ItemDetailCreate


def create_item_detail(
    db: Session, obj_in: ItemDetailCreate, item_id: int, unit_id: int
) -> ItemDetail:
    db_obj = db.query(ItemDetail).filter(
        ItemDetail.description.like(obj_in.description)
    )

    if db_obj:
        return db_obj
    else:
        db_obj = ItemDetail(**obj_in.dict(), item_id=item_id, unit_id=unit_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
