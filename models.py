from peewee import *
import os
from dotenv import load_dotenv 

load_dotenv()

pg_db = PostgresqlDatabase('verceldb', user=os.getenv("USER"), password=os.getenv("PASSWORD"),
                        host=os.getenv("HOST"), port=5432)

class BaseModel(Model):
    class Meta:
        database = pg_db

class Order(BaseModel):
    order_id = AutoField(column_name='order_id')
    product_id = IntegerField(column_name='product_id')
    order_date = TimestampField(column_name='order_date', null=False)
    product_quantity = IntegerField(column_name='product_quantity', null=False)
    order_sum = IntegerField(column_name='order_sum', null=False)

    class Meta:
        table_name = 'orders'
