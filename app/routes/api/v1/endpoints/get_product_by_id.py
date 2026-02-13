from fastapi import APIRouter,Depends
import logging
from app.core.dependecies import get_product_service
from app.services.products import ProductService

router = APIRouter()

@router.get("/get_product_by_id")
async def get_product_by_id(
    id:str,
    service:ProductService = Depends(get_product_service)
        ):
    try:
        response = await service.get_product_by_id(id)
        return response
    except Exception as e:
        logging.error(f"error occured while getting product by id {str(e)}")
        raise e
