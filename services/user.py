from schemas.user import User

from models.user import User as UserModel


class UserService():
    def __init__(self,db) -> None:
        self.db = db
    
    def create_user(self,user:User)-> User:
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return 