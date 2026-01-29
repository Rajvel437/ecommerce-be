
from fastapi import APIRouter,HTTPException,Depends
from app.schemas.users import UserRequest,UserResponse
from app.services.user import userService
import logging
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from app.core.dependecies import get_user_service
from app.services.user import userService
from app.core.exceptions import UserAlreadyExistsException

router = APIRouter()
security=HTTPBearer()


@router.post("/insert_user",response_model=UserResponse)
async def createUser(
    request:UserRequest,
    credentials:HTTPAuthorizationCredentials=Depends(security),
    user_service:userService=Depends(get_user_service)

    ):
    try:
        user_data = await user_service.create_user(
            name=request.name,
            email=request.email,
            phoneNumber=request.phoneNumber,
            password=request.password
        )
        return {"user_data": user_data}
    except HTTPException as e:
        raise e
    except Exception as e:
        logging.error(f"error occured while creating insert_user {str(e)}")
        raise e




