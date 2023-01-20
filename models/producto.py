from config.database import Base
from sqlalchemy import Column,Integer,String,Float,PickleType




class Product(Base):
    __tablename__ = "Productos"

    id = Column(Integer,primary_key = True)
    name = Column(String,nullable=False)
    price = Column(Float,nullable=False)
    stock = Column(Integer)
    image = Column(String)
    
    
