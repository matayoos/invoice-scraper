from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class ItemDetails(Base):
    __tablename__ = "item_details"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    item_id = Column(Integer, ForeignKey("item.id"))
    unit_id = Column(String, ForeignKey("unit.id"))

    item = relationship("Item", back_populates="item_details")
    unit = relationship("Unit", back_populates="item_details")
    invoice_item = relationship("InvoiceItem", back_populates="item_details")
