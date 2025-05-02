'''
Subject: Dukan (Mobile_store_Basemodel file)
Created By: Anup Kumar
Created On: 25.Apr.2025 (Add function)
Modified On: 29.Apr.2025 (Sale function)
'''

from pydantic import BaseModel

class mobilestore(BaseModel):
    seller_name: str
    product_name: str
    product_quantity: int
    product_detail: str | None = None
    product_id: int
    product_price: float

class sale(BaseModel): # creating a BaseModel of sale details
    product_id: int
    quantity_sold: int