from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(String, index=True)
    grocery_store_id = Column(Integer, ForeignKey("grocery_store.id"))

    grocery_store = relationship("GroceryStore", back_populates="item")
    invoice_item = relationship("InvoiceItem", back_populates="item")
    item_detail = relationship("ItemDetail", back_populates="item")
    item_category = relationship("ItemCategory", back_populates="item")
