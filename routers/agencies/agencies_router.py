from fastapi import APIRouter, Depends
import datetime

# local modules
from config.db import get_db
from routers.agencies.agencies_models import AgencyPost
from routers.routers_utils import send200, send500

agencies_router = APIRouter()

@agencies_router.post("")
async def post_agency(agc: AgencyPost, db = Depends(get_db)):
    agencies = db.agencies
    result = await agencies.insert_one({
        **agc.dict(),
        "created_at": datetime.datetime.now(),
        "last_edited_at": datetime.datetime.now()
    })
    return send200({ "inserted_id": str(result.inserted_id)})