from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
    product_id: int
    order_date: datetime
    product_quantity: int
    order_sum: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "product_id": 1,
                    "order_date": "2024-08-23T07:02:18+00:00",
                    "product_quantity": 2,
                    "order_sum": 2222
                }
            ]
        }
    }
