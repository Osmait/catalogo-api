from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.user import User
from config.database import Session
from services.user import UserService
from utils.jwt import create_token
from models.user import User as UserModel




user_router = APIRouter()

@user_router.post("/user",tags=["users"],response_model=dict,status_code=201)
def create_user(user:User):
    
    db = Session()
    UserService(db).create_user(user)
    return {"msg": "successfully created"}


@user_router.post("/login",tags=["users"])
def login(user:User):
    db = Session()
    user_db:UserModel = db.query(UserModel).filter(UserModel.email == user.email).first()

    if not user_db: return JSONResponse(status_code=403, content={"msg": "email of password invalid"})

    if user_db.password != user.password:
        return JSONResponse(status_code=404, content={"msg": "email of password invalid"})

    
    token:str = create_token(jsonable_encoder(user_db))
    return {"token":token}
