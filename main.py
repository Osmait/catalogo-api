from fastapi import FastAPI
from config.database import engine,Base
from router.product import product_router
from router.user import user_router



app = FastAPI()
app.title = "Catalogo"
app.version= "0.0.1"

Base.metadata.create_all(bind=engine)
app.include_router(product_router)
app.include_router(user_router)


