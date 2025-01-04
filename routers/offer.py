from fastapi import APIRouter, Path, HTTPException
from bson import ObjectId
import datetime

# local modules
from models import Offer, Agency
from routers.utils import get_error_details, send200, send404
from routers.constants import HTTP_CODES, ErrorTypes

offers_router = APIRouter()

@offers_router.get("/")
async def get_offers():
    offers = await Offer.find().to_list()
    return send200(offers)

@offers_router.post("/")
async def post_offer(offer: Offer):

    # Check if the agency_id corrisponds to an existing agency
    agency = await agency.find_one(Agency.id == ObjectId(offer.agency_id))
    if not agency:
        return send404(["body", "agency_id"], "Not Found, No matching agency")
    
    res = await offer.insert(new_ofr)
    inserted_id = getattr(res, "inserted_id", None)
    if not inserted_id:
        raise HTTPException(HTTP_CODES[500]["code"])
    return send200({
        "inserted_id": str(res.inserted_id),
        "created_on": str(off["created_on"])
    })
