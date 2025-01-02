from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

# Local modules
from routers.utils import send500

db_client = None

async def init_db():
    global db_client
    if not db_client:
        try:
            db_client = AsyncIOMotorClient("mongodb://localhost:27017") # Establishing the connection to the server
            await init_beanie(database=db_client.bibiane, document_models=[
                "models.agency.Agency", "models.offer.Offer"
            ])
        except ConnectionError as e: # If any connection errors occurs
            return send500(e) # Send a general error mess to the client

async def close_db():
    global db_client
    if db_client:
        db_client.close()
        db_client = None