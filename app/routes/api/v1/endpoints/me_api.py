from fastapi import APIRouter,Depends
from app.schemas.auth import AuthRequest,AuthResponse
from app.services.auth import AuthService
from app.core.dependecies import get_auth_service
from app.models.user import User
from app.core.dependecies import get_current_user
 

router=APIRouter()

@router.get("/me")
async def login(
    service:AuthService = Depends(get_auth_service)
):
    try:
        # token = await service.auth_login(request.email,request.password)
        token = "token not valid"
        return {"msg":"Token generation successful","token":token}
    except Exception as e:
        raise e
