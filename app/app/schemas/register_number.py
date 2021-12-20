from pydantic import BaseModel


class RegisterNumberBase(BaseModel):
    cnpj: str
    inscricao_estadual: str


class RegisterNumberCreate(RegisterNumberBase):
    pass


class RegisterNumberUpdate(RegisterNumberBase):
    pass


class RegisterNumberInDBBase(RegisterNumberBase):
    id: int

    class Config:
        orm_mode = True


class RegisterNumber(RegisterNumberInDBBase):
    pass


class RegisterNumberInDB(RegisterNumberInDBBase):
    pass
