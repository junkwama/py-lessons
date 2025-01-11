from pydantic import BaseModel, Field
from beanie import Document
import datetime

class GeneralSettins:
    max_nesting_depth = 1

class BaseDocument(Document):
    created_on: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_on: datetime.datetime = Field(default_factory=datetime.datetime.now)