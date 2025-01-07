# external modules
from pydantic import Field, BaseModel
from beanie import Document, BackLink, Link, PydanticObjectId
from typing import Optional, List
from enum import Enum
import datetime

class OfferType(Enum):
    studies = "studies"
    immigration = "immigration"
    tourism = "tourisme"

class AgencyBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=256)

class Agency(AgencyBase, Document):
    offers: List[BackLink["Offer"]] = Field(original_field="agency")
    created_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    
    class Settings:
        name = "agencies" # DB collection's name
        max_nesting_depth = 1  # Only fetch linked objects's imediate keys

class Application(Document):
    offer: Link["Offer"]
    created_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    
    class Settings:
        name = "applications"
        
class OfferBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=256)
    description: Optional[str] = Field(None, max_length=3000)
    type: OfferType
    agency_id: PydanticObjectId
    
class Offer(OfferBase, Document):
    applications: List[BackLink["Application"]] = Field(original_field="offer")
    agency: Link["Agency"]
    created_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_on: datetime.datetime = Field(default_factory=datetime.datetime.now)

    class Settings:
        name = "offers"
        