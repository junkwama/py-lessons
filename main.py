# external modules
from fastapi import FastAPI, Request

# local modules
from routers.routers_utils import send200, send500

# Routes 
from routers.offers.offers_router import offers_router
from routers.agencies.agencies_router import agencies_router


app = FastAPI()

# General exceptions are handled here before 
@app.exception_handler(Exception)
def general_exc_handler(request: Request, e: Exception):
    return send500(e)

@app.get("/")
def server_status():
    return send200({
        "app_name": "Bibiane API",
        "version": "1.0.0",
        "status": "Server up running",
        "status_code": 200
    })

# App routes
app.include_router(offers_router, prefix="/offers", tags=["offers"])
app.include_router(agencies_router, prefix="/agencies", tags=["agencies"])