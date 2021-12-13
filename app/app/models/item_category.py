from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class ItemCategory(Base):
    __tablename__ = "item_category"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("item.id"))
    category_id = Column(Integer, ForeignKey("category.id"))

    items = relationship("Item", back_populates="item_category")
    category = relationship("Category", back_populates="item_category")
