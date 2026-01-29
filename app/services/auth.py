from app.models.user import User
from app.database.mssql import db
import logging
from app.core.exceptions import UserNotFoundError,PasswordNotValid
from app.core.security import verify_password
from app.core.jwt import generate_token

class AuthService:
    def __init__(self):
        self.db=db

    async def auth_login(self,email:str,password:str):
        """ Checking user exist or not, if yes return the token """
        try:
            user = self.db.query(User).filter(User.email==email).first()
            if not user:
                logging.error(f"User not found {email}")
                raise UserNotFoundError("email",email)
            logging.debug("User existed,checking password is correct or not")
            isPasswordvalid =await verify_password(password,user.hashedPassword)
            if not isPasswordvalid:
                logging.error("password not matched..")
                raise PasswordNotValid()
            
            logging.info("password matched..,token generating")
            user_data = {
                "id":user.id,
                "email":user.email,
                "phoneNumber":user.phoneNumber,
                "name":user.name
            }

            jwt_token =await generate_token(user_data)
            logging.info("User verification successful, token generated.")

            return jwt_token
        
        except Exception as e:
            logging.error("error occured while performoing login")
            raise e





