from fastapi import APIRouter, Path, HTTPException, Depends, status
import datetime
from bson import ObjectId

# local modules
from config.db import get_db
from routers.offers.offers_models import Offer, OfferBase
from utils.utils import deserialize_id
from routers.routers_utils import HTTP_CODES

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


# print(ofr)


@offers_router.get("")
async def get_offers(db = Depends(get_db)):
    offers_col = db.offers
    offers = await offers_col.find().to_list()
    return [serialize_offer(ofr) for ofr in offers]

@offers_router.post("")
async def post_offer(ofr: OfferBase, db = Depends(get_db)):
    
    agencies = db.agencies
    offers = db.offers
    
    # Check if the agency_id corrisponds to an existing agency
    agc = await agencies.find_one({"_id": deserialize_id(ofr.agency_id)})
    print(agc)
    if not agc:
        raise HTTPException(HTTP_CODES[404])
    new_ofr = {
        **ofr.dict(),
        "agency_id": agc["_id"],
        "created_on": datetime.datetime.now(),
        "last_updated_on": datetime.datetime.now(),
        "applications": []
    }
    
    print(new_ofr)
    
    return None

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

@app.post("/offers")
def post_offers(b_ofr: BaseOffer) -> Offer:
    

    # Creating a proper id to the new offer item
    # With 0 as initial value even if the list is empty we still have 0 + 1
    id = 1 + reduce(lambda cur_res, cur_item: cur_res if cur_res >= cur_item.id else cur_item.id, offers, 0)
    
    # We expand properties of the new BaseOffer and use them to create an new Offer
    ofr = Offer(id=id, **b_ofr.dict())
    
    # Then we add it to the list 
    offers.append(ofr)
    
    return ofr # return the offer with the right id to the user

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