# external libs
from pydantic import BaseModel, Field, validator
from typing import Optional
import datetime

# local libs
from utils.models import OfferType
from utils.utils import is_valid_obj_id

class OfferBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=256)
    type: OfferType
    description: Optional[str] = Field(None, max_length=3000)
    agency_id: str
    
    @validator("agency_id")
    def is_agency_id_valid(cls, v): return is_valid_obj_id(v)


class Offer(OfferBase):
    id: str
    created_on: datetime.datetime
    last_updated_on: datetime.datetime
    applications: list = Field([])
    
    @validator("id")
    def is_id_valid(cls, v): return is_valid_obj_id(v)
    
