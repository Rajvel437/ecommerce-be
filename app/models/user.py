
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer,DateTime,Column,String,func
from app.database.mssql import engine
from app.models.base import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(String(100),primary_key=True,index=True)
    name = Column(String(200),nullable=False)
    email = Column(String(100),unique=True,index=True,nullable=False)
    phoneNumber = Column(String(10),unique=True,index=True,nullable=False)
    createdAt = Column(DateTime,server_default=func.now())
    updatedAt = Column(DateTime,onupdate=func.now())
    hashedPassword = Column(String(500),nullable=False)

