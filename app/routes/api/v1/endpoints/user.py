
from fastapi import APIRouter
from app.schemas.users import UserRequest
from app.services.user import userService

router = APIRouter()


@router.post("/insert_user")
async def createUser(request:UserRequest
                     ):
    try:
        service = userService()
        user_id = await service.create_user(
            name=request.name,
            email=request.email,
            phoneNumber=request.phoneNumber
        )
        return {"user_id": user_id}
    except Exception as e:
        return {"error": str(e)}









