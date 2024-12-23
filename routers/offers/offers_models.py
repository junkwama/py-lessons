# external libs
from pydantic import BaseModel, Field, validator
from typing import Optional
from enum import Enum
from bson import ObjectId
import datetime

# local libs
from utils.utils import is_valid_obj_id

class OfferType(Enum):
    studies = "studies"
    immigration = "immigration"
    tourism = "tourisme"

class OfferBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=256)
    type: OfferType
    description: Optional[str] = Field(None, max_length=3000)
    agency_id: str 
    
    @validator("agency_id")
    def is_agency_id_valid(cls, v): return is_valid_obj_id(v)
    
    def insertable_dict(self):
        this_ofr_dict = self.dict()
        return {
            **this_ofr_dict,
            "agency_id": ObjectId(this_ofr_dict["agency_id"]),
            "type": this_ofr_dict["type"].name,
            "created_on": this_ofr_dict.get("created_on", datetime.datetime.now()),
            "last_updated_on": this_ofr_dict.get("last_updated_on", datetime.datetime.now()),
            "applications": this_ofr_dict.get("applications", [])
        }

class Offer(OfferBase):
    id: str
    created_on: datetime.datetime
    last_updated_on: datetime.datetime
    applications: list = Field([])
    
    def __init__(self, agency_id, _id: Optional[ObjectId] = None):
        # Because fom MongoDB we are getting "agency_id" and "_id"(for Offrer's "id" prop) in ObjectID type
        if  _id: self.id = str(_id) 
        if not isinstance(agency_id, str): self.agency_id = str(agency_id)
    
    @validator("id")
    def is_id_valid(cls, v): 
        if not is_valid_obj_id(v):
            raise ValueError("id string invalid as ObjectId")
        return v
    
