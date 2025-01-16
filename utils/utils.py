import jwt
import traceback
from datetime import datetime, timedelta
from dotenv import load_dotenv 
from typing import Optional
from beanie import PydanticObjectId

from config.config import Config, Env

def log(e):
    exc = traceback.format_exc()
    print(
        "\n***************************************\n", 
        "Error:", exc, "\nDate:", datetime.datetime.now(),
        "\n\nDetails:", "\n--------\n", exc,
        "\n***************************************\n"
    )

def generate_token(
    id: PydanticObjectId, 
    candidate: Optional[dict] = None, 
    admin: Optional[dict] = None
):  
    """ Generate a JWT access token with a payload and expiry. """
    key = Env.BIBIANE_TOKEN_KEY.value
    algorithm = Config.TOKEN_ALGORITHM.value
    exp_days = datetime.now() + timedelta(days=Config.TOKEN_EXPIRATION_DAYS.value)
    payload = {
        "sub": id,
        "exp":  exp_days,
        "role": {
            "candidate": candidate,
            "admin": admin
        }
    }
    
    return jwt.encode(payload, key, algorithm)

def verify_token(token: str):
    """ Verify the validity of a token """
    key =  Env.BIBIANE_TOKEN_KEY.value
    algorithm = Config.TOKEN_ALGORITHM.value
    try:
        return jwt.decode(token, key, algorithm)
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None