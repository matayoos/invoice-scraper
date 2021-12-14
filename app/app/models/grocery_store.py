from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .grocery_store import GroceryStore  # noqa: F401


class GroceryStore(Base):
    __tablename__ = "grocery_store"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cnpj = Column(String, index=True)
    inscricao_estadual = Column(String, index=True)
    address = Column(String, index=True)

    invoice = relationship("Invoice", back_populates="grocery_store")
    item = relationship("Item", back_populates="grocery_store")
