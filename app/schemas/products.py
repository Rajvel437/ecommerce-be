from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import datetime
from typing import List


class ProductPostRequest(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    category: Optional[str] = None
    stock_quantity: int



class ProductPostResponse(BaseModel):
    id: str
    name: str
    description: Optional[str]
    price: Decimal
    currency: str
    category: Optional[str]
    stock_quantity: int
    is_active: bool
    created_at:datetime

    class Config:
        form_attributes:True


    
