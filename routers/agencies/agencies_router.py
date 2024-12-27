from fastapi import APIRouter, Depends, Query
from typing import Optional

# local modules
from config.db import get_db
from routers.agencies.agencies_models import AgencyBase, Agency
from routers.routers_utils import send200

agencies_router = APIRouter()

@agencies_router.post("")
async def post_agency(agc: AgencyBase, db = Depends(get_db)):
    _agencies = db.agencies
    result = await _agencies.insert_one(agc.deserialize())
    return send200({ "inserted_id": str(result.inserted_id)})

@agencies_router.get("")
async def get_agencies(
    db = Depends(get_db), limit: int = Query(10, ge=1, le=100),
    order_by: Optional[str] = Query(None, description="Field to sort by, e.g., 'created_on'"),
    desc: Optional[bool] = Query(False, description="If should sort descending: 'true' or 'false'")
):
    _agencies = db.agencies
    agencies =  _agencies.find()
    
    if limit:
        agencies = agencies.limit(limit)
    if order_by or desc:
        sort_direction = -1 if desc else 1  # 1 for ascending, -1 for descending
        agencies = agencies.sort(order_by or "_id", sort_direction)
    
    agencies = await agencies.to_list()
    
    return send200([Agency(**agc) for agc in agencies])