from fastapi import APIRouter, Path, HTTPException, Depends, status
import datetime
from bson import ObjectId

# local modules
from config.db import get_db
from routers.offers.offers_models import Offer, OfferBase
from utils.utils import deserialize_id
from routers.routers_utils import get_error_details, send200, send404
from routers.router_constants import HTTP_CODES, ErrorTypes

offers_router = APIRouter()

"""
def get_offer_from_list(id):
    return list(filter(lambda _ofr: _ofr.id == id, offers))[0] if offers else null


class OfferType(Enum):
    study = "études"
    immmigration = "immigration"
    bourse = "bourse d'études"
    
class BaseOffer(BaseModel): 
    type: OfferType
    title: str = Field(..., max_length=1024)
    agency_id: int = Field(..., gt=0)

class UpdateBaseOffer(BaseModel):
    type: Optional[OfferType] = None
    title: Optional[str] = Field(None, max_length=1024)
    agency_id: Optional[int] = Field(None, gt=0)    

class Offer(BaseOffer):
    id: int = Field(..., gt=0)
    apl_nbr: int = Field(0, ge=0)
    
    def update(self, ub_ofr: UpdateBaseOffer):
        items = list(ub_ofr.dict().items())
        ofr = next((_ofr for _ofr in offers if _ofr.id == self.id), None)
        if ofr:
            for key, val in items:
                if val:
                    setattr(ofr, key, val)
    
    def delete(self):
        global offers # To avoid confusion with the local var offers
        offers = list(filter(lambda ofr: ofr.id != self.id, offers))
"""

# f = {
#     "_id": ObjectId("676916a829eec0cc8e9c6de1"),
#     "title": "Etudier au Canada",
#     "type": "studies",
#     "description": "Nous vous accompagnons dans vos demarches pour realiser votre projet d'etudes au canada",
#     "created_on": datetime.datetime.fromisoformat("2024-12-23T08:52:08.864Z"),
#     "last_updated_on": datetime.datetime.fromisoformat("2024-12-23T08:52:08.864Z"),
#     "applications": [],
#     "agency_id": ObjectId("6761e26fd959a3aefa9b4452")
# }


# o = Offer(**f)

# print(o)

@offers_router.get("")
async def get_offers(db = Depends(get_db)):
    _offers = db.offers
    offers = await _offers.find().to_list()
    return [Offer(**ofr) for ofr in offers]

@offers_router.post("")
async def post_offer(ofr: OfferBase, db = Depends(get_db)):
    _agencies = db.agencies
    offers = db.offers
    
    # Check if the agency_id corrisponds to an existing agency
    agc = await _agencies.find_one({"_id": deserialize_id(ofr.agency_id)})
    if not agc:
        return send404(["body", "agency_id"], "Not Found, No matching agency")
    
    # Insert the new agency to the data base
    new_ofr = ofr.insertable_dict()
    res = await offers.insert_one(new_ofr)
    inserted_id = getattr(res, "inserted_id", None)
    if not inserted_id:
        raise HTTPException(HTTP_CODES[500]["code"])
    return send200({
        "inserted_id": str(res.inserted_id),
        "created_on": str(new_ofr["created_on"])
    })

"""

@app.get("/offers")
def get_offers(type: Optional[OfferType] = None, min_apl_nbr: Optional[int] = None, order_by: Optional[str] = None, limit: Optional[int] = None):
    _offers = list(offers)
    
    # Only take those with a specific application number
    if (type):
        _offers = list(filter(lambda ofr: ofr.type == type, offers))
    
    # only take those with a certain min appliction number
    if (min_apl_nbr):
        _offers = list(filter(lambda ofr: ofr.apl_nbr >= min_apl_nbr, _offers))
    
    # Soert according to the value of "order_by" params
    if (order_by):
        # ofr.dict()[order_by]: first we convert it to a dict then we accest the value of the give order by field
        _offers.sort(key=lambda ofr: ofr.dict()[order_by], reverse=True) 
    
    # limit to a specific number of items    
    if (limit):
        _offers = _offers[:limit]
    
    return _offers


@app.get("/offers/{id}")
def get_offer(*, id: int = Path(..., gt=0)) -> Offer:
    
    ofr = get_offer_from_list(id)
    if not ofr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inexisting offer")
    
    # Otherwise we send the requested offer.
    return ofr


@app.put("/offers/{id}")
def put_offer(*, id: int = Path(..., gt=0), updated_ofr: UpdateBaseOffer):
    ofr = get_offer_from_list(id)
    if ofr:
        ofr.update(updated_ofr)
        return ofr
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inexisting offers")

@app.delete("/offers/{id}")
def delete_offer(*, id: int = Path(..., gt=0)) -> Offer:
    ofr = get_offer_from_list(id)
    if ofr:
        ofr.delete()
        return ofr
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inexisting offers")

"""