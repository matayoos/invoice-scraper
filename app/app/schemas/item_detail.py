from pydantic import BaseModel


class ItemDetailBase(BaseModel):
    description: str
    item_id: int
    unit_id: int


class ItemDetailCreate(ItemDetailBase):
    pass


class ItemDetailUpdate(ItemDetailBase):
    pass


class ItemDetailInDBBase(ItemDetailBase):
    id: int

    class Config:
        orm_mode = True


class ItemDetail(ItemDetailInDBBase):
    pass


class ItemDetailInBase(ItemDetailInDBBase):
    pass
