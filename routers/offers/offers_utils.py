# External libs
from pydantic import BaseModel, Field
import datetime

# Local libs
from utils.models import OfferType

# initial_offers = [{"id": 1, "type": "études", "title": "Étudier au canada", "agency_id": 2, "apl_nbr": 3}]

class Offer(BaseModel):
    id: str
    title: str = Field(..., min_length=2, max_length=256)
    type: OfferType
    agency_id: str
    applications: list = Field([])
    created_on: datetime.datetime
    last_updated_on: datetime.datetime
    
    
class OfferPost(BaseModel):
    title: str = Field(..., min_length=2, max_length=256)
    type: OfferType
    agency_id: str