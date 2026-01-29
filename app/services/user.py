from app.database.mssql import db
from app.models.user import User
import uuid
from fastapi import HTTPException
import logging
import bcrypt
from app.core.exceptions import UserAlreadyExistsException


class userService:
    def __init__(self):
        self.db = db

    async def create_user(self,name:str,
                          email:str,
                          phoneNumber:str,
                          password:str
                          ):
        try:
            user = db.query(User).filter(User.email==email).first()
            if user:
                raise UserAlreadyExistsException(field="email",value=email)
            raw_password =await self._hash_password(password)
            new_user = User(
                id = str(uuid.uuid4()),
                name=name,
                email=email,
                phoneNumber=phoneNumber,
                hashedPassword=raw_password
                 )

            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            dict1={}
            for column in new_user.__table__.columns:
                dict1[column.name] = str(getattr(new_user, column.name))
            return dict1
        except Exception as e:
            logging.error(f"error occured while creating user {str(e)}")
            raise e


    async def _hash_password(self,raw_password: str) -> str:
        try:
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(
                raw_password.encode("utf-8"),  # ✅ convert to bytes
                salt
            )
            return hashed_password.decode("utf-8")  # ✅ store as string
        except Exception as e:
            logging.error(f"Error while hashing password: {str(e)}")
            raise e






