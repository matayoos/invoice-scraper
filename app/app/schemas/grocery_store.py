from pydantic import BaseModel


class GroceryStoreBase(BaseModel):
    name: str
    cnpj: str
    inscricao_estadual: str
    address: str


class GroceryStoreCreate(GroceryStoreBase):
    pass


class GroceryStoreUpdate(GroceryStoreBase):
    pass


class GroceryStoreInDBBase(GroceryStoreBase):
    id: int

    class Config:
        orm_mode = True


class GroceryStore(GroceryStoreInDBBase):
    pass


class GroceryStoreInDB(GroceryStoreBase):
    pass
