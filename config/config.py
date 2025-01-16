from enum import Enum


class Config(Enum): 
    ITEMS_PER_PAGE = 10
    TOKEN_EXPIRATION_DAYS = 7
    TOKEN_ALGORITHM = "HS256"
    
    
class Env(Enum):
    BIBIANE_ENV="development"
    BIBIANE_TOKEN_KEY="o?Bx?qE~P\"^69pT"