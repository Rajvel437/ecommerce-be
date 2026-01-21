from fastapi import APIRouter
from app.routes.api.v1.endpoints.user import router as user_router

api_router = APIRouter()

api_router.include_router(user_router,prefix="/v1",tags=["Register"])
