from pydantic import BaseModel


class UnitBase(BaseModel):
    name: str


class UnitCreate(UnitBase):
    pass


class UnitUpdate(UnitBase):
    pass


class UnitInDBBase(UnitBase):
    id: int

    class Config:
        orm_mode = True


class Unit(UnitInDBBase):
    pass


class UnitInDB(UnitInDBBase):
    pass
