from pydantic import BaseModel, Field, validator, computed_field
from beanie import PydanticObjectId, Link, Indexed
from passlib.context import CryptContext
from typing import Optional
from enum import Enum
from datetime import date

from models.items import Admin, Candidate
from models.subs import Address, Contacts
from models.utils import BaseDocument, GeneralSettins

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRole(Enum):
    SUPERMANAGER = "SUPERMANAGER" # SUPER SYSTEM MANAGER
    MANAGER = "MANAGER" # SYSTEM ADMINS
    PARTNER = "PARTNER" # AGENCY PARTNER ADMINS
    ADMIN = "ADMIN" # AGENCIES CLASSIC ADMINS
    CANDIDATE = "CANDIDATE" # CANDIATES

class Gender(Enum):
    MAN = "M"
    WOMAN = "F"
    
class UserAuth(BaseModel):
    email: Indexed(str, unique=True) =  Field(
        ..., 
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", 
        examples=["jeanmarc@example.com"], 
        description="Email address"
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        examples=["Ag?1*nv67"],
        description="Password must include at least one uppercase letter, one lowercase letter, one digit, and one special character."
    )
    
    def hash_password(self):
        self.password = password_context.hash(self.password)
        
    def does_password_match(self, password):
        return password_context.verify(password, self.password)
        
    @validator("password")
    def validate_password(cls, value):
        # Ensure at least one uppercase letter
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter.")
        # Ensure at least one lowercase letter
        if not any(char.islower() for char in value):
            raise ValueError("Password must contain at least one lowercase letter.")
        # Ensure at least one digit
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit.")
        # Ensure at least one special character
        special_characters = "@$!%*?&"
        if not any(char in special_characters for char in value):
            raise ValueError(f"Password must contain at least one special character: {special_characters}")
        return value

class UserBase(UserAuth):
    firstname: str = Field(..., max_length=64, min_length=2, examples=["Jean Marc"], description="The user's firsname")
    lastname: str = Field(..., max_length=64, min_length=2, examples=["Mulamba"], description="The user's lastname")
    middlename: Optional[str] = Field(None,  max_length=64, min_length=2, examples=["Matwiudi"], description="The user's middlename")
    gender: Gender = Field(..., examples=["M"], description="Gender of the user. 'F' or 'M' are accepted")
    birthdate: Optional[date] = Field(
        None,
        description="The user's date of birth. Must be a valid date in the past.",
        examples=["1990-01-01"]
    )

    class Settings(GeneralSettins):
        name = "users"
    
class User(UserBase, BaseDocument):
    role: UserRole = Field(UserRole.CANDIDATE.value) # for now we assume they're all candidates)
    username: Indexed(str, unique=True) = Field(
        None,
        min_length=3,  # Minimum username length
        max_length=30,  # Maximum username length
        pattern=r"^[a-zA-Z0-9_.-]+$",  # Restricts to alphanumeric characters, underscores, periods, and hyphens
        examples=["jean12_"],
        description="A unique username consisting of 3 to 30 characters, allowing letters, numbers, underscores, periods, and hyphens."
    )
    contacts: Optional[Contacts] = Field(None, description="Contact informations")
    address: Optional[Address] = Field(None, description="Address informations")

    # some candidate field
    candidate: Optional[Link["Candidate"]] = Field(None)
    admin: Optional[Link["Admin"]] = Field(None)

    def is_candidate():
        return 