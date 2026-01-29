from pydantic import BaseModel
from typing import Optional


class UserRequest(BaseModel):
    name:str
    email:str
    phoneNumber:str
    password:str

class UserModel(BaseModel): 
    id: str
    name: str
    email: str
    phoneNumber: str
    createdAt: str
    updatedAt: Optional[str]

    class Config:
        form_attributes=True


class UserResponse(BaseModel):
    user_data:UserModel




