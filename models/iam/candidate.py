from pydantic import Field
from beanie import BackLink
from typing import List

# NB: THIS FILE CANNOT CALL ANYTHING FROM models/iam/user to avaoid circule dependency
from models.utils import BaseDocument, GeneralSettins
from models.items import Application

class Candidate(BaseDocument):
    applications: List[BackLink["Application"]] = Field(original_field="candidate")
    
    class Settings(GeneralSettins):
        name = "candidates"
