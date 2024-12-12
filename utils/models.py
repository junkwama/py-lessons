from bson import ObjectID as BsonObjectId
from enum import Enum

# Id is a string that can be convert to an Bson's ObjectID
# That why we have resplaced the validation function used by the classic str class 
# To a one that checks if the str is convertable to ObectID
class Id(str):
    @classmethod
    def __get__validators__(cls):
        yield cls.validate
        
    @classmethod
    def validate(cls, value):
        if not BsonObjectId.is_valid(value): # if the str is convertable to an bson object ID
            raise ValueError("String invalid as Bson's ObjectID")
        return v
    
class OfferType(Enum):
    STUDIES = "Études"
    IMMIGRATION = "Immigration"
    TOURISM = "Tourisme"
    

