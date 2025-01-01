from beanie import Document
from pydantic import Field, BaseModel
import datetime

class AgencyBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=256)

class Agency(AgencyBase, Document):
    created_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    
    class Settings:
        name = "agencies"
