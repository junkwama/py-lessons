# External modules
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError

# Local modules
from routers.utils import send200, send500, send422
from config.db import init_db, close_db

# Routes 
from routers.offer.index import offers_router
from routers.agency.index import agencies_router

app = FastAPI()

# with motor initialize db and link it to beanie
@app.on_event("startup")
async def on_startup():
    await init_db()

# close the connection on shutdown
@app.on_event("shutdown")
async def on_shutdown():
    await close_db()

# Exceptions reprocessed and formated bfr bein' sent to the client 
# General 500 exceptions
@app.exception_handler(Exception)
def exc_handler_500(request: Request, e: Exception): # NB: even when we don't use request we must put it because he func expect it 
    return send500(e)

# 422 Pydantic check fails
@app.exception_handler(RequestValidationError)
def exc_handler_422(request: Request, e: RequestValidationError):
    error_location = None  
    error_message = None
    try:
        error = e.errors()[0]
        error_location = error["loc"]
        error_message = error["msg"]
    finally: 
        return send422(error_location, error_message)

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