
from pydantic import BaseModel, Field
from utils.models import Id

initial_offers = [{"id": 1, "type": "études", "title": "Étudier au canada", "agency_id": 2, "apl_nbr": 3}]

def serialize_offer(offer):
    if offer:
        offer["_id"] = str(offer["_id"]) # Convert the mondoDB ObjectID into a string id
    return offer 

class Offer(BaseModel):
    id: Optional[Id] = Field(None, alias="_id")
    # created_on: date,
    # last_updated_on: date,
    title: str = Field(..., gt=2, lt=256)
    agency_id: Id
    applications: Optional[list] = Field([])