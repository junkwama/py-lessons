from pydantic import BaseModel
from bson import ObjectId
import datetime
from beanie import Document

# Serializing: When I am sending data to client
# Deserialize: When I am saving data to DB
# Dataused by python are static to one specific type, Fixe data missmatch in constructor.

class Base(Document):
    
    # Gen classes config
    class Config:
        arbitrary_types_allowed = True # Accept custom class as Pydantic props type
        json_encoders = { 
            ObjectId: str,  # Convert ObjectId to str during serialization
            datetime.datetime: lambda v: v.isoformat()  # Serialize datetime as ISO format
        }