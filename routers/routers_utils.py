# External modules
from fastapi import status
from fastapi.responses import JSONResponse
from typing import Optional, Any

# Local modules
from utils.utils import log
from routers.router_constants import HTTP_CODES, ErrorTypes

def get_error_details(
    type: Optional[str] = None, loc: Optional[list] = None, 
    msg: Optional[str] = None, input: Optional[Any] = None
) -> dict: return { "type": type, "loc": loc, "msg": msg, "input": input }


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
    
    return JSONResponse(content, code)

def send200(data): 
    return send(data)

def send404(error_location: list, error_message: Optional[str] = None): 
    return send(
        error_message = error_message or HTTP_CODES[404]["message"],
        error_type = ErrorTypes.not_found_error,
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

def send500(e: Exception):
    if e: log(e)
    return send(error_message = HTTP_CODES[500]["message"], code = HTTP_CODES[500]["code"])