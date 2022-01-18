from pydantic import BaseModel


class InvoiceSeriesBase(BaseModel):
    series_number: str


class InvoiceSeriesCreate(InvoiceSeriesBase):
    pass


class InvoiceSeriesUpdate(InvoiceSeriesBase):
    pass


class InvoiceSeriesInDBBase(InvoiceSeriesBase):
    id: int

    class Config:
        orm_mode = True


class InvoiceSeries(InvoiceSeriesInDBBase):
    pass


class InvoiceSeries(InvoiceSeriesInDBBase):
    pass


class InvoiceSeriesInDB(InvoiceSeriesInDBBase):
    pass
