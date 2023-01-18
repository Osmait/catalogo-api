from pydantic import Field,BaseModel
from typing import Optional


class Product(BaseModel):
    name:str = Field(min_length=3, max_length=255)
    price:int = Field(ge=1)
    stock:Optional[int] = 0
    image:Optional[str]= None


    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Ropa",
                "price": 2000,
                "stock": 10,
                "image":""
                
            }
        }