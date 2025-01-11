from pydantic import BaseModel, Field, validator
from beanie import PydanticObjectId, Link, Indexed
from typing import Optional
from enum import Enum
from datetime import date

from models.subs import Address, Contacts
from models.utils import BaseDocument

class Role(Enum):
    SUPERMANAGER = "SUPERMANAGER" # SUPER SYSTEM MANAGER
    MANAGER = "MANAGER" # SYSTEM ADMINS
    PARTNER = "PARTNER" # AGENCY PARTNER ADMINS
    ADMIN = "ADMIN" # AGENCIES CLASSIC ADMINS
    CANDIDATE = "CANDIDATE" # CANDIATES

class Gender(Enum):
    MAN = "M"
    WOMAN = "F"

class UserBase(BaseModel):
    firstname: str = Field(..., max_length=64, min_length=2, examples="Jean Marc", description="The user's firsname")
    lastname: str = Field(..., max_length=64, min_length=2, examples="Mulamba", description="The user's lastname")
    middlename: Optional[str] = Field(None,  max_length=64, min_length=2, examples="Matwiudi", description="The user's middlename")
    gender: Gender = Field(..., examples="M", description="Gender of the user. 'F' or 'M' are accepted")
    contacts: Optional[Contacts] = Field(None, description="Contact informations")
    Address: Optional[Address] = Field(None, description="Address informations")
    birthdate: Optional[date] = Field(
        None,
        description="The user's date of birth. Must be a valid date in the past.",
        example="1990-01-01"
    )
    email: Indexed(str, unique=True) =  Field(
        ..., 
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", 
        example="jeanmarc@example.com", 
        description="Email address"
    )
    password: str = Field(
        ...,
        pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,64}$",
        description="Password must be 8-64 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.",
        example="P@ssw0rd123"
    )
    
class User(UserBase, BaseDocument):
    role: Role
