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
    agency_id: ObjectId 
    
    class Config:
        arbitrary_types_allowed = True # Accept custom class as Pydentic props type
        json_encoders = { # When serializing ObjectId instances, use str(obj)
            ObjectId: str
        }
    
    def deserialize(self):
        this = self.dict()
        return {
            **this,
            "type": this["type"].name,
            "created_on": this.get("created_on", datetime.datetime.now()),
            "updated_on": this.get("updated_on", datetime.datetime.now()),
            "applications": this.get("applications", [])
        }

class Offer(OfferBase):
    id: ObjectId = Field(alias="_id") # alias _id because from db, they are coming as _id
    created_on: datetime.datetime
    updated_on: datetime.datetime
    applications: list = Field([])

