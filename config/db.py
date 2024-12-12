from fastapi import Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient

async def get_db():
    
    # Establishing the connection to the server
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    
    try:
        
        # Triyng to retrieving and yield (return) an updated version of the "bibiane" database
        yield client.bibiane
        
    except ConnectionError as e: # If any connection errors occurs
        
        print("Database connectoun Error:", str(e)) # Tell the api devs what happened
        
        # Send a general error mess to the client
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="The connection to the DB failed"
        )
        
    finally:
        
        # Always close the connection of efficiency
        client.close()