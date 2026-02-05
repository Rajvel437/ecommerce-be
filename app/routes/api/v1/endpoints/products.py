from fastapi import APIRouter,Depends
import logging
from app.schemas.products import ProductPostRequest,ProductPostResponse
from app.services.products import ProductService
from app.core.dependecies import get_product_service

router = APIRouter()

@router.post("/products",response_model=ProductPostResponse)
async def create_product(
    request:ProductPostRequest,
    service:ProductService = Depends(get_product_service)

):
    try:
        response =await service.create_product(request.name,
                                          request.description,  
                                          float(request.price),
                                            request.category,
                                            request.stock_quantity)
        return response
    
    except Exception as e:
        logging.error(f"error occured while creating product {str(e)}")
        raise e

