# External modules
from pydantic import Field
from beanie import Document, BackLink
from typing import Optional
import datetime

class Application(Document):
    offer: Optional[BackLink["Offer"]] = Field(original_field="applications")
    created_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    
    class Settings:
        name = "applications"