from config.database import Base
from sqlalchemy import Column,Integer,String,Float


class Product(Base):
    __tablename__ = "Productos"

    id = Column(Integer,primary_key = True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    image = Column(String)
    
    
