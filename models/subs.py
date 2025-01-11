from pydantic import BaseModel, Field, validator
from typing import Optional

from utils.countries import COUNTRIES

class Address(BaseModel):
    country: str = Field(..., max_length=3, min_length=3, examples=["afg", "cod", "usa"], description="The alpha-3 ISO code of the country")
    street: str = Field(..., max_length=100, example=["Elmo"], description="The name of the street")
    house_number: str = Field(..., max_length=10,  example=["12B"], description="The house or apartment number")
    city: str = Field(..., max_length=50, example=["Springfield"], description="The city")
    state_province: Optional[str] = Field(None, max_length=50, example=["Illinois"], description="The state or province. Optional for countries without states.")
    postal_code: Optional[str] = Field(..., pattern=r"^\d{5}(-\d{4})?$", example=["62704"], description="The ZIP or postal code for the address")
    full_address: Optional[str] = Field(None, max_length=255, min_length="2", example=["123 Elm Street"], description="The full address")
    
    @validator("country")
    def validate_country(cls, value):
        if not value in COUNTRIES:
            raise ValueError("Must enter a valid and existing country alpha-3 iso code. E.g: 'cod' for Dr Congo, 'afg' for Afganistan.")
        return value

class Contacts(BaseModel):
    phone: Optional[str] = Field(None, pattern=r"^\+?[1-9]\d{1,14}$", example=["+24381567890"], description="Main phone number")
    phone2: Optional[str] = Field(None, pattern=r"^\+?[1-9]\d{1,14}$", example=["+24489876954"], description="Secondary phone number")
    whatsapp: Optional[str] = Field(None, pattern=r"^\+?[1-9]\d{1,14}$", example=["+908871567890"], description="WhatsApp number")
    email: Optional[str] = Field(None, pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", example=["johndoe@example.com"], description="Email address")

