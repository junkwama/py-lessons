import traceback
import datetime

from bson import ObjectId

def log(e):
    exc = traceback.format_exc()
    print(
        "\n***************************************\n", 
        "Error:", exc, "\nDate:", datetime.datetime.now(),
        "\n\nDetails:", "\n--------\n", exc,
        "\n***************************************\n"
    )

def is_valid_obj_id(v):
    if not ObjectId.is_valid(v):
        raise ValueError("String invalid as ObjectId")
    return v

def deserialize_id(str_id: str) -> ObjectId:
    try: return ObjectId(str_id)
    except: return None
    
def serialize_id(mongo_id: ObjectId) -> str:
    try: return str(mongo_id)
    except: return None