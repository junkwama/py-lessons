from fastapi import APIRouter, Query, Path
from beanie import PydanticObjectId, BackLink

# local modules
from models import Agency, AgencyBase
from routers.utils import send200, send404, send422
from config.config import Config

agencies_router = APIRouter() 

@agencies_router.post("/")
async def post_agency(agency_base: AgencyBase):
    agency = Agency(**agency_base.dict())
    result = await agency.insert()
    return send200({ "inserted_id": str(result.id)})

@agencies_router.get("/")
async def get_agencies(
    limit: int = Query(10, ge=1, le=100),
    order_by: str = Query(None, description="Field to sort by, e.g., 'created_on'"),
    desc: bool = Query(False, description="If should sort descending: 'true' or 'false'")
):
    agencies =  Agency.find(fetch_links=True).limit(limit or Config.ITEMS_PER_PAGE.value)
    if order_by or desc:
        sort_direction = -1 if desc else 1  # 1 for ascending, -1 for descending
        agencies = agencies.sort((order_by or "created_on", sort_direction))
    
    agencies = await agencies.to_list()

    # print(agencies[0].offers[0])
    
    return send200(agencies)

@agencies_router.get("/{id}")
async def get_agency(id: PydanticObjectId = Path(...)):
    agency = await Agency.get(id)
    if not agency:
        return send404(["query", "id"], "agency not found")
    return send200(agency)