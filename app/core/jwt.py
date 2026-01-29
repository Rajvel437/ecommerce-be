
import jwt
from datetime import datetime, timedelta,timezone
from app.config import settings
from jwt import ExpiredSignatureError,InvalidTokenError
from fastapi import HTTPException


async def generate_token(user_data:dict)-> str:
    try:
        encoded_data = user_data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        encoded_data.update({"exp":expire})
        token = jwt.encode(user_data,key="ecommerce",algorithm="HS256")
        return token
    except Exception as e:
        raise e

async def decode_token(token:str)->dict:
    try:
        payload = jwt.decode(token,key="ecommerce",algorithms="HS256")
        return payload
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token expired"
        )

    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    except Exception as e:
        raise e




