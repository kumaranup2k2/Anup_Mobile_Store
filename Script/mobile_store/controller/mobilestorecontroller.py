'''
Subject: Dukan (Mobile_Store_Controller file)
Created By: Anup Kumar
Created On: 25.Apr.2025 (Add function)
Modified On: 27.Apr.2025 (Delete function)
Modified On: 29.Apr.2025 (Sale function)
'''

from fastapi import FastAPI, HTTPException
from mobile_store.model.mobilemodel import mobilestore, sale
from mobile_store.service.productservice import ProductService

app = FastAPI()

list_of_product = []

@app.post("/item/create")   #Product add hoga
async def add_product(product: mobilestore):
    for myproduct in list_of_product:# Pehle check karenge ki product_id duplicate hai ya nhi
        if product.product_id == myproduct.product_id:
            raise HTTPException(status_code=400,detail=f"Item '{myproduct.product_id}' already exists. Unable to create")# Agar product already exist karta hai to error aayega
    list_of_product.append(product)# Agar product unique hai to usko list me add kar denge
    return {"message": "Product added successfully","product": product}

@app.put("/item/updateQuantity/{product_id}")  # product ka quantity update
async def update_product_quantity(product_id: int, quantity_to_add: int):
    product_service = ProductService()
    try:
        response = product_service.update_product_quantity(product_id, quantity_to_add)
        return {"message": f"Product ID {product_id} quantity updated successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error on updating quantity: {e}")

@app.delete("/item/delete/{product_id}")    # Product_id ka use kr k product ko delete kr rhe hai
async def delete_product(product_id: int):
    for myproduct in list_of_product:
        if myproduct.product_id == product_id:# Pehle check karenge ki product_id hai ya nhi
            list_of_product.remove(myproduct)
            return
        else:
            return ("Product_id not Found!!!!!")

@app.post("item/addSale{product_id}")# Product_id ka use kr k product ko sale kr rhe hai
async def add_sale(sale: sale):
    product_service = ProductService()
    try:
        product_service.add_sale(sale, product_id = int, quantity_sold= int)  # service method ko Call krenge sala data add krenge
        return # Return success response
    except ValueError as e:# Any error adding sale
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/item/allProducts")#view data
async def get_all_products():
    service = ProductService()
    products = service.view_product(product_id=int)
    return {"products": products}#table return