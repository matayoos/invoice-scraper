from pydantic import BaseModel


class ItemCategoryBase(BaseModel):
    item_id: int
    category_id: int


class ItemCategoryCreate(ItemCategoryBase):
    pass


class ItemCategoryUpdate(ItemCategoryBase):
    pass


class ItemCategoryInDBBase(ItemCategoryBase):
    id: int

    class Config:
        orm_mode = True


class ItemCategoryInDBBase(ItemCategoryInDBBase):
    pass


class ItemCategory(ItemCategoryInDBBase):
    pass


class ItemCategoryDB(ItemCategoryInDBBase):
    pass
