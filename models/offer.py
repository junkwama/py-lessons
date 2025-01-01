# external libs
from pydantic import Field, BaseModel
from beanie import Document
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

class Offer(Document):
    
    agency_id: str
    title: str = Field(..., min_length=2, max_length=256)
    description: Optional[str] = Field(None, max_length=3000)
    type: OfferType
    applications: list = Field(default_factory=list)
    created_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_on: datetime.datetime = Field(default_factory=datetime.datetime.now)

    class Settings:
        name = "offers"


