from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import Numeric
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class InvoiceItems(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("item.id"))
    invoice_id = Column(Integer, ForeignKey("invoice.id"))
    qty = Column(Numeric, index=True)
    value = Column(Numeric, index=True)

    items = relationship("Items", back_populates="invoice_items")
    invoices = relationship("Invoice", back_populates="invoice_items")
