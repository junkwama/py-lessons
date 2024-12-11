from fastapi import Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure

async def get_db():
    
    # Establishing the connection to the server
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    
    try:
        
        # Triyng to retrieving and yield (return) an updated version of the "bibiane" database
        yield client.bibiane
        
    except ConnectionError:
        
        # If any connection errors occurs
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            description="The connection to DB failed"
        )
        
    finally:
        
        # Always close the connection of efficiency
        client.close()