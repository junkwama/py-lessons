from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional
from pydantic import BaseModel, Field, validator
from enum import Enum
from functools import reduce

app = FastAPI()

###

available_agencies = [{"id": 1, "name": "BeRDC"}, {"id": 2, "name": "Best Travels"}]

# First we have a list of diction for available offers
initial_offers = [{"id": 1, "type": "études", "title": "Étudier au canada", "agency_id": 2, "apl_nbr": 3}]

def get_offer_from_list(id):
    return list(filter(lambda _ofr: _ofr.id == id, offers))[0] if offers else null

###


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

# We convert the existing offers from dictionaris to the Offer format we prepare with the Offer Modal above
offers = [Offer(**ofr_dict) for ofr_dict in initial_offers]

@app.get("/")
def get_index():
    return [{"data": "Helooo from fast-api"}]

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
    
    # Check if the agency_id corrisponds to an existing agency
    if not any(agc["id"] == b_ofr.agency_id for agc in available_agencies):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Inexisting agency")
    
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