
from fastapi import status
from fastapi.responses import JSONResponse
from typing import Optional, Any

# local moduls
from utils.utils import log

HTTP_CODES = {
    200: status.HTTP_200_OK,
    400: status.HTTP_400_BAD_REQUEST,
    401: status.HTTP_401_UNAUTHORIZED,
    403: status.HTTP_403_FORBIDDEN,
    404: status.HTTP_404_NOT_FOUND,
    409: status.HTTP_409_CONFLICT,
    500: status.HTTP_500_INTERNAL_SERVER_ERROR
}

def send(
    data: Optional[Any] = None, error_message: Optional[str] = None,
    code: Optional[int] = 200, error_location: Optional[str] = None,
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

def send500(e: Exception):
    if e: log(e)
    return send(error_message = "An error while processing your request", code = 500)