from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class RegisterNumber(Base):
    __tablename__ = "register_number"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String, index=True, unique=True)
    inscricao_estadual = Column(String, index=True, unique=True)

    grocery_store = relationship("GroceryStore", back_populates="register_number")
