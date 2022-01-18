from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class GroceryStore(Base):
    __tablename__ = "grocery_store"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    register_number_id = Column(Integer, ForeignKey("register_number.id"))

    register_number = relationship("RegisterNumber", back_populates="grocery_store")
    invoice = relationship("Invoice", back_populates="grocery_store")
    item = relationship("Item", back_populates="grocery_store")
    type_store = relationship("TypeStore", back_populates="grocery_store")
