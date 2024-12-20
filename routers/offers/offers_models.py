# external libs
from pydantic import BaseModel, Field, validator
from typing import Optional
from enum import Enum
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
            "type": str(this_ofr_dict["type"]),
            "created_on": this_ofr_dict.get("created_on", datetime.datetime.now()),
            "last_updated_on": this_ofr_dict.get("last_updated_on", datetime.datetime.now()),
            "applications": this_ofr_dict.get("applications", [])
        }


class Offer(OfferBase):
    id: str
    created_on: datetime.datetime
    last_updated_on: datetime.datetime
    applications: list = Field([])
    
    @validator("id")
    def is_id_valid(cls, v): return is_valid_obj_id(v)
    
