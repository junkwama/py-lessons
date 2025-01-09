# External Moduls
from fastapi import APIRouter, HTTPException

# Local modules
from models import Offer, ApplicationBase, Application
from routers.utils import send200, send404
from routers.constants import HTTP_CODES

applicatlions_router = APIRouter()

@applicatlions_router.get("/")
async def get_applications():
    applications = await Application.find(fetch_links=True).to_list()
    print(applications)
    #return send200(applications)

@applicatlions_router.post("/")
async def post_application(application_base: ApplicationBase):
    # Check if the offer_id corrisponds to an existing offer
    offer = await Offer.get(application_base.offer_id)
    if not offer:
        return send404(["body", "offer_id"], "Not Found, No matching offer")
    # If the offer exists, then procede
    application = Application(offer=offer, **application_base.dict())
    inserted_application = await application.insert()
    if not inserted_application.id:
        raise HTTPException(HTTP_CODES[500]["code"])
    return send200({
        "inserted_id": str(inserted_application.id),
        "created_on": str(inserted_application.created_on)
    })