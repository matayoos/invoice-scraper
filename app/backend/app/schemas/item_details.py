from pydantic import BaseModel


class ItemDetailsBase(BaseModel):
    description: str


class ItemDetailsCreate(ItemDetailsBase):
    pass


class ItemDetaislUpdate(ItemDetailsBase):
    pass


class ItemDetailsInDBBase(ItemDetailsBase):
    id: int

    class Config:
        orm_mode = True


class ItemDetails(ItemDetailsInDBBase):
    pass


class ItemDetailsInBase(ItemDetailsInDBBase):
    pass
