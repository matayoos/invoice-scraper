from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import Numeric
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class InvoiceItem(Base):
    __tablename__ = "invoice_item"

    id = Column(Integer, primary_key=True, index=True)
    item_details_id = Column(Integer, ForeignKey("item_details.id"))
    invoice_id = Column(Integer, ForeignKey("invoice.id"))
    qty = Column(Numeric, index=True)
    value = Column(Numeric, index=True)

    item_details = relationship("ItemDetails", back_populates="invoice_item")
    invoice = relationship("Invoice", back_populates="invoice_item")
