from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Pessoa(Base):
    __tablename__ = "pessoa"

    id = Column(UUID, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
