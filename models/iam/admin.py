from beanie import Link

from models.utils import GeneralSettins, BaseDocument
from models.items import Agency

class Admin(BaseDocument):
    agency: Link["Agency"]
    
    class Settings(GeneralSettins):
        name = "admins"
        