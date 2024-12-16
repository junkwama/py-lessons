
from fastapi import Response, status
from pydantic import Field
from typing import Optional, Any

HTTP_CODES = {
    200: status.HTTP_200_OK,
    400: status.HTTP_400_BAD_REQUEST,
    401: status.HTTP_401_UNAUTHORIZED,
    403: status.HTTP_403_FORBIDDEN,
    404: status.HTTP_404_NOT_FOUND,
    409: status.HTTP_409_CONFLICT,
    500: status.HTTP_500_INTERNAL_SERVER_ERROR
}

def send(responce_obj: Response, data, error_mess: Optional[str] = None, code: Optional[int] = Field(200), error_field: Optional[str] = None):
    
    content = {
        "code": code,
        "data": data or None, 
        "error": { 
            "message": error_mess, 
            "field": error_field 
        } if (error_mess or error_field) else None
    }

    if code != 200:
        responce_obj.status_code = HTTP_CODES[code]
    
    return content

def send200(responce_obj: Response, data):
    return send(responce_obj, data)

def send500(responce_obj: Response):
    return send(responce_obj, None, "An error while processing your request", 500)