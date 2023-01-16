from fastapi import APIRouter,Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.producto import Product
from config.database import Session
from services.product import ProductService
from typing import List



product_router = APIRouter()

@product_router.post("/product",tags=["product"],response_model=dict, status_code=201)
def create_product(product:Product) -> dict:
    db = Session()
    ProductService(db).create_product(product)
    return {"msg":"successfully created"}


@product_router.get("/product",tags=["product"],response_model=List[Product],status_code=200)
def get_products()-> List[Product]:
    db = Session()
    result = ProductService(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@product_router.get("/product/{id}",tags=["product"],response_model=Product,status_code=200)
def get_product_byId(id:int =Path(ge=1)) ->Product:
    db = Session()
    result = ProductService(db).get_movie_byId(id)
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@product_router.put("/product{id}",tags=["product"],response_model=dict,status_code=200)
def update_product(id:int,product:Product)-> dict:
    db = Session()
    result = ProductService(db).get_movie_byId(id=id)
    if not result:
        return JSONResponse(status_code=404, content={"msg":"not found"})
    ProductService(db).update_product(id,product)
    return JSONResponse(status_code=200,content={"msg":"successfully Update"})

@product_router.delete("/product{id}",tags=["product"],response_model=dict,status_code=200)
def delete_product(id:int)-> dict:
    db = Session()
    result:Product = ProductService(db).get_movie_byId(id=id)
    if not result:
        return JSONResponse(status_code=404,content={"msg":"no found"})
    ProductService(db).delete_product(id)
    return JSONResponse(status_code=200,content={"msg":"Delete Product"})


    
