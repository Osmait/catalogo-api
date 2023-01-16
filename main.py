from fastapi import FastAPI
from config.database import engine,Base
from router.product import product_router



app = FastAPI()
app.title = "Catalogo"
app.version= "0.0.1"

Base.metadata.create_all(bind=engine)
app.include_router(product_router)

