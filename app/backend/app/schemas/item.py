from pydantic import BaseModel


class ItemBase(BaseModel):
    item_id: str


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class ItemInDBBase(ItemBase):
    id: int

    class Config:
        orm_mode = True


class Item(ItemInDBBase):
    pass


class ItemInDB(ItemInDBBase):
    pass
