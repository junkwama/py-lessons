from fastapi import APIRouter
from models import UserAuth, UserBase, User
from routers.utils import send400, send200
from datetime import datetime

from routers.user import create_user

auth_router = APIRouter()

@auth_router.post("")
async def auth(user_auth: UserAuth):
    user = await User.find_one(User.email == user_auth.email, fetch_links=True)
    if not user or not user.check_password(user_auth.password): 
        return send400(error_location="Password or username incorrect") 
    return send200({
        "created_on": datetime.now(),
        "token": {
            "data": user.get_token(),
            "type": "bearer"
        }
    })

@auth_router.post("/register")
async def post_user(user_base: UserBase): 
    return await create_user(user_base)