from schemas.producto import Product
from models.producto import Product as ProductModel
from repository.product_repository import ProductRepository


class ProductService():
    def __init__(self) -> None:
        self.repository = ProductRepository()

    def create_product(self,product:Product):
        self.repository.create(product)
        return
    
    def get_movies(self):
        result = self.repository.get_all()
        return result
    
    def get_movie_byId(self,id):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return result

    def update_product(self,id:int,data:Product):
        product = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        product.name = data.name
        product.price = data.price
        product.stock = data.stock
        self.db.commit()
        return

    def delete_product(self,id:int):
        self.db.query(ProductModel).filter(ProductModel.id == id).delete()
        self.db.commit()
        return
