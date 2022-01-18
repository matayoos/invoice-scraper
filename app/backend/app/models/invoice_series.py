from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class InvoiceSeries(Base):
    __tablename__ = "invoice_series"

    id = Column(Integer, primary_key=True, index=True)
    series_number = Column(String, index=True)

    invoice = relationship("Invoice", back_populates="invoice_series")
