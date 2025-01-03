# external modules
from pydantic import Field, BaseModel
from beanie import Document, BackLink, Link
from typing import Optional, List
from enum import Enum
import datetime

class OfferType(Enum):
    studies = "studies"
    immigration = "immigration"
    tourism = "tourisme"

class Offer(Document):
    title: str = Field(..., min_length=2, max_length=256)
    description: Optional[str] = Field(None, max_length=3000)
    type: OfferType
    applications: Optional[List[Link["Application"]]]
    agency: BackLink["Agency"] = Field(original_field="offers")

    created_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_on: datetime.datetime = Field(default_factory=datetime.datetime.now)

    class Settings:
        name = "offers"