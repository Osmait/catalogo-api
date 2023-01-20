from fastapi import APIRouter, Path, UploadFile,Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.producto import Product
from config.database import Session
from services.product import ProductService
from typing import List
from middelware.jwt_bearer import JWTBearer

import random

from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary


cloudinary.config(
    cloud_name="divez9sgt",
    api_key="534463164334522",
    api_secret="lbWU3NzsQFuDWnLnrHMQD59H3LM",
    secure=True
)


product_router = APIRouter()


@product_router.post("/product", tags=["product"], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_product(product: Product) -> dict:
    """_summary_

    Args:
        product (Product): _description_

    Returns:
        dict: _description_
    """
    db = Session()
    ProductService(db).create_product(product)
    return {"msg": "successfully created"}


@product_router.get("/product", tags=["product"], response_model=List[Product], status_code=200)
def get_products() -> List[Product]:
    db = Session()
    result =  ProductService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@product_router.get("/product/{id}", tags=["product"], response_model=Product, status_code=200)
def get_product_byId(id: int = Path(ge=1)) -> Product:
    db = Session()
    result = ProductService(db).get_movie_byId(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@product_router.put("/product{id}", tags=["product"], response_model=dict, status_code=200,dependencies=[Depends(JWTBearer())])
def update_product(id: int, product: Product) -> dict:
    db = Session()
    result = ProductService(db).get_movie_byId(id=id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "not found"})
    ProductService(db).update_product(id, product)
    return JSONResponse(status_code=200, content={"msg": "successfully Update"})


@product_router.delete("/product{id}", tags=["product"], response_model=dict, status_code=200,dependencies=[Depends(JWTBearer())])
def delete_product(id: int) -> dict:
    db = Session()
    result: Product = ProductService(db).get_movie_byId(id=id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "no found"})
    ProductService(db).delete_product(id)
    return JSONResponse(status_code=200, content={"msg": "Delete Product"})


@product_router.post("/uploadfile/{id}", tags=["product"], response_model=dict, status_code=200)
def create_file(file: List[UploadFile] , id):
    db = Session()
    conten = file.file.read()
    name_image = file.filename.split(".")[0]
    extencion = ["jpg", "png"]
    if file.filename.split(".")[1] not in extencion:

        return JSONResponse(status_code=400, content={"msg": "extencion no valida"})

    imagen_id = f"{random.randrange(1,21020)}-{name_image}"
    upload(conten, public_id=imagen_id)
    url, _ = cloudinary_url(imagen_id, width=400, height=400, crop="fill")
    result = ProductService(db).get_movie_byId(id=id)
    result.image = url
  
    db.commit()
    return JSONResponse(status_code=200, content={"msg": "successfully Update"})

    # try:
    #     if not os.path.exists("upload"):
    #         os.mkdir("upload")
    #     with open(f"upload/{file.filename}","wb")as f:
    #         f.write(conten)
    # except Exception as e:
    #     return {"message":"Erro Uploading file"}
    # finally:
    #     file.file.close()
