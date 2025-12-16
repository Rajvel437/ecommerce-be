
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer,DateTime,Column,String,func
from app.database.mssql import engine

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"

    id = Column(String(100),primary_key=True,index=True)
    name = Column(String(200))
    email = Column(String(100),unique=True,index=True)
    phoneNumber = Column(String(10),unique=True,index=True)
    createdAt = Column(DateTime,server_default=func.now())
    updatedAt = Column(DateTime,onupdate=func.now())


Base.metadata.create_all(bind=engine)

