from fastapi import APIRouter,Depends
import logging
from app.schemas.products import ProductPostResponse
from typing import List
from app.services.products import ProductService
from app.core.dependecies import get_product_service

router = APIRouter()



@router.get("/get_products",response_model=List[ProductPostResponse])
async def get_products(
    offset:int,limit:int,category:str,
    service:ProductService = Depends(get_product_service)
):
    try:
        response =await service.fetch_all_products(offset,limit,category)
        return response
    except Exception as e:
        logging.error(f"error occured while getting products {str(e)}")
        raise e











