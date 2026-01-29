from sqlalchemy import Integer,Column,String,DECIMAL,DateTime,Boolean,func
from app.models.base import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(String(100),primary_key=True,index=True)
    name = Column(String(255),nullable=False)
    description = Column(String,nullable=True)
    price = Column(DECIMAL(10,2),nullable=False)
    currency = Column(String(10),default="INR",nullable=False)
    category = Column(String(100),nullable=True,index=True)
    stock_quantity = Column(Integer, default=0,nullable=False)
    is_active = Column(Boolean, default=True,nullable=False,index=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())





