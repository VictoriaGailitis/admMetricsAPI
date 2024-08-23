from fastapi import FastAPI
import uvicorn
from models import Order
import schemas
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

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
        query = Order.select().order_by(Order.order_id).dicts()
        return {'orders':list(query)}
    except:
        return {'error': "no records in table"}

@app.post("/orders")
def create_order(data: schemas.Order):
    try:
        try:
            query = list(Order.select().order_by(Order.order_id).dicts())
            order_id = query[len(query)-1]["order_id"] + 1
        except:
            order_id = 1
        order = Order.create(order_id=order_id, product_id=data.product_id, order_date=f'{data.order_date :%Y-%m-%d %H:%M:%S}', 
                        product_quantity=data.product_quantity, order_sum=data.order_sum)
        order.save()
        return {'status': "ok"}
    except:
        return {"status": "error"}

if __name__ == "__main__":
    uvicorn.run(app)
