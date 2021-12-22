from sqlalchemy.orm.session import Session

from app import crud, schemas
from .utils import insert, get_content


def register_invoice(db: Session, url: str):
    try:
        content = get_content.get_invoice_info(url)

        grocery_store_id = insert.insert_grocery_store_info(
            db, obj_in=content["grocery_store"]
        )

        invoice_id = insert.insert_invoice_info(
            db, obj_in=content["invoice"], grocery_store_id=grocery_store_id
        )

        insert.insert_invoice_items(db, content["items"], grocery_store_id, invoice_id)

        return crud.get_invoice_by_id(db, id=invoice_id)

    except:
        pass
