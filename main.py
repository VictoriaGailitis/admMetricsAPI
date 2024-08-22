from fastapi import FastAPI
import uvicorn
from models import Order
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/orders")
def get_orders():
    try:
        query = Order.select().order_by(Order.product_id).dicts()
        return {'orders':list(query)}
    except:
        return {'error': "no records in table"}


if __name__ == "__main__":
    uvicorn.run(app)
