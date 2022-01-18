from sqlalchemy.orm import Session

from app.models.item_details import ItemDetails
from app.schemas.item_details import ItemDetailsCreate


def create_item_details(
    db: Session, obj_in: ItemDetailsCreate, item_id: int, unit_id: int
) -> int:
    db_obj = (
        db.query(ItemDetails)
        .filter(ItemDetails.description.like(obj_in.description))
        .first()
    )

    if db_obj:
        return db_obj.id
    else:
        db_obj = ItemDetails(**obj_in.dict(), item_id=item_id, unit_id=unit_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj.id
