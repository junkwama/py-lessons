import traceback
from datetime import datetime, timedelta

from config.config import Config, Env

def log(e):
    exc = traceback.format_exc()
    print(
        "\n***************************************\n", 
        "Error:", exc, "\nDate:", datetime.now(),
        "\n\nDetails:", "\n--------\n", exc,
        "\n***************************************\n"
    )

get_token_exp = lambda: datetime.now() + timedelta(days=Config.TOKEN_EXPIRATION_DAYS.value)

def verify_token(token: str):
    """ Verify the validity of a token """
    key =  Env.BIBIANE_TOKEN_KEY.value
    algorithm = Config.TOKEN_ALGORITHM.value
    try:
        return jwt.decode(token, key, algorithm)
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None