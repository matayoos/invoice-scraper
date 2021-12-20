from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Numeric
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Invoice(Base):
    __tablename__ = "invoice"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    date_time = Column(DateTime, index=True)
    access_key = Column(String, index=True)
    auth_protocole = Column(String, index=True)
    nfce_number = Column(String, index=True)
    final_value = Column(Numeric, index=True)
    discount = Column(Numeric, index=True)
    grocery_store_id = Column(Integer, ForeignKey("grocery_store.id"))
    series_id = Column(Integer, ForeignKey("invoice_series.id"))

    grocery_store = relationship("GroceryStore", back_populates="invoice")
    invoice_item = relationship("InvoiceItem", back_populates="invoice")
    invoice_series = relationship("InvoiceSeries", back_populates="invoice")
