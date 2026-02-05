from fastapi import APIRouter,Depends
from app.routes.api.v1.endpoints import user,auth,me_api,products,get_products
from app.core.dependecies import get_current_user


api_router = APIRouter()


api_router.include_router(user.router,prefix="/v1",tags=["Register User"])
api_router.include_router(auth.router,prefix="/v1",tags=["Auth"])
api_router.include_router(me_api.router,prefix="/v1",tags=["Me"],dependencies=[Depends(get_current_user)])
api_router.include_router(
    prefix="/v1",
    router=products.router,
    tags=["Products"],
    dependencies=[Depends(get_current_user)]
)
api_router.include_router(get_products.router,prefix="/v1",tags=["Products"])



