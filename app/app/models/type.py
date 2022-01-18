from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Type(Base):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    type_store = relationship("TypeStore", back_populates="type")
