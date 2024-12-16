from pydantic import BaseModel
import datetime

class Agency(BaseModel):
    id: str
    name: str
    created_at: datetime.datetime
    last_edited_at: datetime.datetime

class AgencyPost(BaseModel):
    name: str
    