from pydantic import BaseModel
from beanie import Document, Indexed
from typing import Optional
import pymongo 

class Category(BaseModel):
    name: str
    description: str

class Product(Document):
    name: str                          # You can use normal types just like in pydantic
    description: Optional[str] = None
    price: Indexed(float, pymongo.ASCENDING)              # You can also specify that a field should correspond to an index
    category: Category                 # You can include pydantic models as well
