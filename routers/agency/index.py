from fastapi import APIRouter, Query, Path
from bson import ObjectId

# local modules
from models.agency import Agency, AgencyBase
from routers.utils import send200, send404, send422

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
    agencies =  Agency.find()
    if limit:
        agencies = agencies.limit(limit)
    if order_by or desc:
        sort_direction = -1 if desc else 1  # 1 for ascending, -1 for descending
        agencies = agencies.sort((order_by or "created_on", sort_direction))
    
    agencies = await agencies.to_list()
    
    return send200(agencies)

@agencies_router.get("/{id}")
async def get_agency(id: str = Path(...)):
    
    # Check if the sent "id" is valid inother to send a proper 422 intead of a automatic 500 by fastapi
    if not ObjectId.is_valid(id):
        return send422(["query", "id"], "id field is invalid")
    
    # If the sent id is valid, search the db
    agency = await Agency.find_one(Agency.id == ObjectId(id))
    if not agency:
        return send404(["query", "id"], "agency not found")
    return send200(agency)