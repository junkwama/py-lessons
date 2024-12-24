from pydantic import BaseModel, Field
from bson import ObjectId
import datetime

class AgencyBase(BaseModel):
    name: str
    
    class Config:
        arbitrary_types_allowed = True # Accept custom class as Pydantic props type
        json_encoders = { # When serializing ObjectId instances, use str(obj)
            ObjectId: str
        }
    
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
