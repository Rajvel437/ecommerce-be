# from app.database.mssql import get_db_connection

from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.mssql import DB
from app.services.user import userService
from app.services.auth import AuthService
from functools import lru_cache
from fastapi.security import OAuth2PasswordBearer
from app.models.user import User
from app.core.jwt import decode_token
from app.core.exceptions import UserNotFoundError
import logging

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


def get_db()->Session:
    db = DB.get_db_connection()
    try:
        yield db
    finally:
        db.close()


@lru_cache
def get_user_service()->userService:
    """ Get user service instance """
    return userService()

@lru_cache 
def get_auth_service()->AuthService:
    """ Get Auth Service instance """
    return AuthService()

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload =await decode_token(token)

    if payload is None:
        raise UserNotFoundError()

    user_id = payload.get("id")
    if not user_id:
        raise UserNotFoundError()

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise UserNotFoundError()
    logging.info(f"Current user fetched: {user.email}")

    return user
