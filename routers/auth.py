from fastapi import APIRouter, Path
from models import UserAuth

auth_router = APIRouter()

@auth_router.post("")
async def auth(user_auth: UserAuth):
    print(user_auth)
    return