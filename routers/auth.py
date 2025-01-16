from fastapi import APIRouter, Path
from models import UserAuth, UserBase

from routers.user import create_user

auth_router = APIRouter()

@auth_router.post("")
async def auth(user_auth: UserAuth):
    print(user_auth)
    return

@auth_router.post("/register")
async def post_user(user_base: UserBase): 
    return await create_user(user_base)
