from app.schemas.type import TypeBase, TypeInDBBase
from pydantic import BaseModel


class TypeStoreBase(BaseModel):
    grocery_store_id: int
    type_id: int


class TypeStoreCreate(TypeStoreBase):
    pass


class TypeStoreUpdate(TypeBase):
    pass


class TypeStoreInDBBase(TypeBase):
    id: int

    class Config:
        orm_mode = True


class TypeStore(TypeStoreInDBBase):
    pass


class TypeStoreInDB(TypeInDBBase):
    pass
