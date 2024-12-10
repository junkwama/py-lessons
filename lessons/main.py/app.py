from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_route():
    return {"data": "Helooo from fast-api"}