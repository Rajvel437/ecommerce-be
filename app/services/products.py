from app.database.mssql import db
import logging
from app.models.product import Product
import uuid

class ProductService:

    def __init__(self):
        self.db = db

    async def create_product(self,name:str,description:str,price:float,category:str,stock_quantity:int):
        try:
            id = str(uuid.uuid4())

            product = Product(
                id = id,
                name = name,
                description=description,
                price=price,
                category=category,
                stock_quantity=stock_quantity
            )

            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product

        except Exception as e:
            logging.error(f"error occured while creating product {str(e)}")
            raise e

    async def fetch_all_products(self,offset:int,limit:int,category:str):
        try:
            query = self.db.query(Product)
            query = query.filter(Product.is_active==True)
            if category:
                query = query.filter(Product.category==category)
            query = query.order_by(Product.created_at)
            
            query = query.offset(offset).limit(limit)

            product_records = query.all()

            return product_records
        except Exception as e:
            logging.error(f"error occured while fecthing all products {str(e)}")
            raise e
        

