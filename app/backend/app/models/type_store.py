from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class TypeStore(Base):
    __tablename__ = "type_store"

    id = Column(Integer, primary_key=True, index=True)
    grocery_store_id = Column(Integer, ForeignKey("grocery_store.id"))
    type_id = Column(Integer, ForeignKey("type.id"))

    grocery_store = relationship("GroceryStore", back_populates="type_store")
    type = relationship("Type", back_populates="type_store")
