from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Unit(Base):
    __tablename__ = "unit"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    item_detail = relationship("ItemDetail", back_populates="unit")
