from pydantic import BaseModel

class TypeBase(BaseModel):
    name: str


class TypeCreate(TypeBase):
    pass


class TypeUpdate(TypeBase):
    pass


class TypeInDBBase(TypeBase):
    id: int

    class Config:
        orm_mode = True


class Type(TypeInDBBase):
    pass


class TypeInDB(TypeInDBBase):
    pass