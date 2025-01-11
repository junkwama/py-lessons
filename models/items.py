# External moduls
from pydantic import Field, BaseModel
from beanie import BackLink, Link, PydanticObjectId
from typing import Optional, List
from enum import Enum
import datetime

# Local moduls
from models.utils import BaseDocument, GeneralSettins

class OfferType(Enum):
    studies = "studies"
    immigration = "immigration"
    tourism = "tourisme"

class AgencyBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=256)

class Agency(AgencyBase, BaseDocument):
    offers: List[BackLink["Offer"]] = Field(original_field="agency")
    
    class Settings(GeneralSettins):
        name = "agencies" # DB collection's name

class ApplicationBase (BaseModel):
    #candidate_id: PydanticObjectId
    offer_id: PydanticObjectId

class Application(ApplicationBase, BaseDocument):
    offer: Link["Offer"]
    
    class Settings(GeneralSettins):
        name = "applications"
        
class OfferBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=256)
    description: Optional[str] = Field(None, max_length=3000)
    type: OfferType
    agency_id: PydanticObjectId
    
class Offer(OfferBase, BaseDocument):
    applications: List[BackLink["Application"]] = Field(original_field="offer")
    agency: Link["Agency"]

    class Settings(GeneralSettins):
        name = "offers"