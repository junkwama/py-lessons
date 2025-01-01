from fastapi import FastAPI, Path
from testler.models import Product, Category
from config.db import init_db, close_db
from routers.utils import send200

from bson import ObjectId

app = FastAPI()

# with motor initialize db and link it to beanie
@app.on_event("startup")
async def on_startup():
    await init_db()

# close the connection on shutdown
@app.on_event("shutdown")
async def on_shutdown():
    await close_db()


# This is an asynchronous example, so we will access it from an async function
@app.post("/")
async def post_product():

    # chocolate = Category(name="Chocolate", description="A preparation of roasted and ground cacao seeds.")
    # tonybar = Product(name="Tony's", price=5.95, category=chocolate)
    # inserted_product = await tonybar.insert() 
    
    # You can find documents with pythonic syntax
    product = await Product.find_one(Product.price < 10)
    print(product)

    return send200(product)

    # And update them
    # await product.set({Product.name:"Gold bar"})

@app.get("/{id}")
async def get_product(id: str = Path(...)):
    product = await Product.find_one(Product.id == ObjectId(id))
    print(product)
    return send200(product)
                      