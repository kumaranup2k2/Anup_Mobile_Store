'''
Subject: Dukan (Dukan Main file)
Created By: Anup Kumar
Created On: 25.Apr.2025 (Add function)
Modified On: 27.Apr.2025 (Delete function)
Modified On: 29.Apr.2025 (Sale function)
Modified On: 30.Apr.2025(Solve Issues)
'''

from fastapi import FastAPI, HTTPException
from mobile_store.model.mobilemodel import mobilestore, sale
from mobile_store.service.productservice import ProductService

app = FastAPI()

list_of_product = []

@app.post("/item/createProduct")#create product
async def add_product(product: mobilestore):
    productService = ProductService()# Pehle check karenge ki product_id duplicate hai ya nhi
    for myproduct in list_of_product:
        if product.product_id == myproduct.product_id:# Agar 400 error means duplicate data hai
            raise HTTPException(status_code=400, detail=f"Product '{product.product_id}' already exists.")
    list_of_product.append(product)# Agar koi duplicate_id nahi mila to product list me add hoga

    try:
        productService.add_product(product)
    except Exception as e:
        print(f"Internal Server Error: {e}")
    return {"message": "Product added successfully"}

@app.delete("/item/deleteProduct")#Product delete
async def delete_product(product_id: int):
    product_service = ProductService()#product check kr rha hai mila to delete
    try:
        product_service.delete_product(product_id)
        return {"message": f"Product with ID {product_id} deleted successfully"}
    except ValueError as e:
        print(f"Product ID {product_id} Not Found Please Recheck And Try Again ")

@app.post("/item/saleproduct")#product sale
async def add_sale(sale: sale):
    product_service = ProductService()
    try:# Call service method to add sale
        product_service.add_sale(sale)
        return {"message": "Sale recorded successfully!"}
    except ValueError as e:# Issue with sale
        print(f"Bad Request: {e}")

@app.get("/item/viewproduct/{product_id}")  # view product
async def get_product_by_id(product_id: int):
    product_service = ProductService()
    try: #product check
        product = product_service.view_product(product_id)
        if product:
            return {"product": tuple(product)}
        else:
            raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")