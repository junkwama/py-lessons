# External moduls
from pydantic import Field, BaseModel
from beanie import BackLink, Link, PydanticObjectId
from typing import Optional, List
from enum import Enum
import datetime

# Local moduls

# CANNOT IMPORT FROM ITEMS TO AVOID CIRCULAR DEPS
from models.utils import BaseDocument, GeneralSettins


# PART 1: ITEMS

class OfferType(Enum):
    studies = "studies"
    immigration = "immigration"
    tourism = "tourisme"

class AgencyBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=256)

class Agency(AgencyBase, BaseDocument):
    offers: List[BackLink["Offer"]] = Field(original_field="agency")
    admins: List[BackLink["Admin"]] = Field(original_field="agency")
    
    class Settings(GeneralSettins):
        name = "agencies" # DB collection's name

class ApplicationBase (BaseModel):
    # candidate_id: PydanticObjectId
    offer_id: PydanticObjectId

class Application(ApplicationBase, BaseDocument):
    offer: Link["Offer"]
    candidate: Link["Candidate"]
    
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
        

# PART 2: Candidate and Admins models put here to avoid circular dependancy

class Admin(BaseDocument):
    agency: Link["Agency"]
    
    class Settings(GeneralSettins):
        name = "admins"
        
class Candidate(BaseDocument):
    applications: List[BackLink["Application"]] = Field(original_field="candidate")
    
    class Settings(GeneralSettins):
        name = "candidates"