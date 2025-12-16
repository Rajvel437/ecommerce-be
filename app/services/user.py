from app.database.mssql import db
from app.models.user import User
import uuid


class userService:
    def __init__(self):
        self.db = db

    async def create_user(self,name:str,
                          email:str,
                          phoneNumber:str
                          ):
        try:
            new_user = User(
                id = str(uuid.uuid4()),
                name=name,
                email=email,
                phoneNumber=phoneNumber
            )

            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return new_user.id
        except Exception as e:
            raise e




