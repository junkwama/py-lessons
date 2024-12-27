from pydantic import Field
from bson import ObjectId
import datetime

# Local modules
from utils.models import Base

class AgencyBase(Base):
    name: str
    
    def deserialize(self):
        this = self.dict()
        return {
            **this,
            "created_on": this.get("created_on", datetime.datetime.now()),
            "updated_on": this.get("updated_on", datetime.datetime.now()),
        }

class Agency(AgencyBase):
    id: ObjectId = Field(alias="_id")
    created_on: datetime.datetime
    updated_on: datetime.datetime
    
