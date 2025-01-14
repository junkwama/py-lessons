# External moduls
from fastapi import APIRouter, HTTPException
from beanie import WriteRules

# Local modules
from models import User, UserBase, UserRole, Candidate
from routers.utils import HTTP_CODES, send200

users_router = APIRouter()

@users_router.get("/")
async def get_users():
    users = User.find()
    users = await users.to_list()
    return send200(users)

@users_router.post("/")
async def post_user(user_base: UserBase):
    
    user = User(**user_base.dict())
    
    # Decide if it's a candidate or a admin
    # Until we implement Auth we only support candidate creation
    candidate = Candidate()
    user.candiate = candidate
    
    # Insert the new user with link_rule to write for any subs Docs like ()
    user = await user.insert(link_rule=WriteRules.WRITE)
    
    if not user.id:
        raise HTTPException(HTTP_CODES[500]["code"])
    return send200({
        "inserted_id": str(user.id),
        "created_on": str(user.created_on)
    })
