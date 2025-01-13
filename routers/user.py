# External moduls
from fastapi import APIRouter, HTTPException

# Local modules
from models import User, UserBase
from routers.utils import send200
from routers.utils import HTTP_CODES

users_router = APIRouter()

@users_router.get("/")
async def get_users():
    users = User.find()
    users = await users.to_list()
    return send200(users)
    
@users_router.post("/")
async def post_user(user_base: UserBase):
    user = User(**user_base.dict())
    
    if not user.id:
        raise HTTPException(HTTP_CODES[500]["code"])
    return send200({
        "inserted_id": str(user.id),
        "created_on": str(user.created_on)
    })
