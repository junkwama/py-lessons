from fastapi import APIRouter, Path, HTTPException
from bson import ObjectId
import datetime
from beanie import BackLink

# local modules
from models import Offer, OfferBase, Agency
from routers.utils import get_error_details, send200, send404
from routers.constants import HTTP_CODES, ErrorTypes

offers_router = APIRouter()

@offers_router.get("/")
async def get_offers():
    offers = await Offer.find(fetch_links=True).to_list()
    return send200(offers)

@offers_router.post("/")
async def post_offer(offer_base: OfferBase):
    # Check if the agency_id corrisponds to an existing agency
    agency = await Agency.get(offer_base.agency_id)
    if not agency:
        return send404(["body", "agency_id"], "Not Found, No matching agency")
    # If the agency exists, then procede
    offer = Offer(agency=agency, **offer_base.dict())
    inserted_offer = await offer.insert()
    if not inserted_offer.id:
        raise HTTPException(HTTP_CODES[500]["code"])
    return send200({
        "inserted_id": str(inserted_offer.id),
        "created_on": str(inserted_offer.created_on)
    })