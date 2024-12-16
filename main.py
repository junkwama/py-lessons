# External libs
from fastapi import FastAPI

# Routes 
from routers.offers.offers_router import offers_router
from routers.agencies.agencies_router import agencies_router


app = FastAPI()

@app.get("/")
def server_status():
    return {
        "name": "Bibiane API",
        "version": "1.0.0",
        "status": "Server up running",
        "status_code": 200
    }

app.include_router(offers_router, prefix="/offers", tags=["offers"])
app.include_router(agencies_router, prefix="/agencies", tags=["agencies"])