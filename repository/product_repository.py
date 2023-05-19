
from config.database import Session
from schemas.producto import Product
from models.producto import Product as ProductModel
class ProductRepository:
    def __init__(self) -> None:
        self.db = Session()

    def get_all(self):
        result = self.db.query(ProductModel).all()
        return result
    
    def create(self,product:Product):
        new_product = ProductModel(**product.dict())
        self.db.add(new_product)
        self.db.commit()
        return