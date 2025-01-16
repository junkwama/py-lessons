# External modules
from pydantic import BaseModel
from bson import ObjectId
from fastapi.responses import JSONResponse
from beanie import BackLink, Link, PydanticObjectId
from fastapi.encoders import jsonable_encoder
from typing import Optional, Any

# Local modules
from utils.utils import log
from routers.constants import HTTP_CODES, ErrorTypes

def get_error_details(
    type: Optional[str] = None, loc: Optional[list] = None, 
    msg: Optional[str] = None, input: Optional[Any] = None
) -> dict: return {"type": type, "loc": loc, "msg": msg, "input": input}


# This function recursively search and parses everything. 
# Since the classic jsonable_encoder doesn't support things BackLinks, ..ect
def jsonable_parser(obj): 
    if isinstance(obj, (BackLink, Link)): return None # return obj.to_dict()
    elif isinstance(obj, (ObjectId, PydanticObjectId)): return str(obj)
    elif isinstance(obj, BaseModel): return jsonable_parser(obj.dict())
    elif isinstance(obj, dict): return {key: jsonable_parser(value) for key, value in obj.items()}
    elif isinstance(obj, list): 
        if all(isinstance(item, (BackLink, Link)) for item in obj)  and len(obj): return None # Instead of returning a list of None, just return None
        return [jsonable_parser(item) for item in obj]
    else: return jsonable_encoder(obj)

def send(
    data: Optional[Any] = None, error_message: Optional[str] = None,
    code: Optional[int] = HTTP_CODES[200]["code"], error_location: Optional[str] = None,
    error_field: Optional[str] = None, error_type: Optional[str] = None
):

    content = {
        "code": code,
        "data": data,
        "error": {
            "type": error_type,
            "message": error_message,
            "location": error_location,
            "field": error_field
        } if (error_type or error_message or error_field or error_location) else None
    }
    
    return JSONResponse(jsonable_parser(content), code)

def send200(data): 
    return send(data)

def send404(error_location: list, error_message: Optional[str] = None): 
    return send(
        error_message = error_message or HTTP_CODES[404]["message"],
        error_type = ErrorTypes.not_found_error.name,
        code = HTTP_CODES[404]["code"],
        error_location = error_location,
        error_field = error_location[-1]
    )

def send422(error_location: list, error_message: Optional[str] = None): 
    return send(
        error_message = error_message or HTTP_CODES[422]["message"],
        error_type = ErrorTypes.validation_error.name,
        code = HTTP_CODES[422]["code"], 
        error_location = error_location,
        error_field = error_location[-1]
    )

def send409(error_location: list, error_message: Optional[str] = None): 
    return send(
        error_message = error_message or HTTP_CODES[409]["message"],
        error_type = ErrorTypes.database_error.name,
        code = HTTP_CODES[409]["code"], 
        error_location = error_location,
        error_field = error_location[-1]
    )

def send500(e: Exception):
    if e: log(e)
    return send(error_message = HTTP_CODES[500]["message"], code = HTTP_CODES[500]["code"])