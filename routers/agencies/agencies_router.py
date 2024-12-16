from fastapi import APIRouter, Depends, status, HTTPException, Response
import datetime

# local modules
from utils.utils import log
from config.db import get_db
from routers.agencies.agencies_models import Agency, AgencyPost
from routers.routers_utils import send200, send500

agencies_router = APIRouter()

@agencies_router.post("")
async def post_agency(responce: Response, agc: AgencyPost, db = Depends(get_db)):
    try:
        agencies = db.agencies
        result = await agencies.insert_one({
            **agc.dict(),
            "created_at": datetime.datetime.now(),
            "last_edited_at": datetime.datetime.now()
        })
        return send200(responce, { "inserted_id": str(result.inserted_id)})  
    
    except Exception as e:
        log(e)
        return send500(responce)
