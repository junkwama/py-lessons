from fastapi import APIRouter, Depends
import datetime

# local modules
from config.db import get_db
from routers.agencies.agencies_models import AgencyBase, Agency
from routers.routers_utils import send200, send500

agencies_router = APIRouter()

@agencies_router.post("")
async def post_agency(agc: AgencyBase, db = Depends(get_db)):
    _agencies = db.agencies
    result = await _agencies.insert_one(agc.deserialize())
    return send200({ "inserted_id": str(result.inserted_id)})

@agencies_router.get("")
async def get_agencies(db = Depends(get_db)):
    _agencies = db.agencies
    agencies = await _agencies.find().to_list()
    return send200(Agency(**agencies[0]).dict())