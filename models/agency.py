from beanie import Document, Link
from pydantic import Field, BaseModel
from typing import Optional, List
import datetime

class AgencyBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=256)

class Agency(AgencyBase, Document):
    offers: Optional[List[Link["Offer"]]]
    created_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    
    class Settings:
        name = "agencies"
