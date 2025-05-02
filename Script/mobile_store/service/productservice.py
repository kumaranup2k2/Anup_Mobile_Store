'''
Subject: Dukan (Product_service file)
Created By: Anup Kumar
Created On: 25.Apr.2025
modified On: 27.Apr.2025 (delete function)
Modified On: 29.Apr.2025 (Sale function,update_quantity)
Modified On: 30.Apr.2025(Solve Issues)
'''

from mobile_store.repository.mobilestoreRepo import ProductRepo

class ProductService:
    def __init__(self):
        pass

    def add_product(self, product, product_name, product_quantity):
        mobilestoreRepo = ProductRepo()
        for myproduct in mobilestoreRepo.get_list():# Pehle check karenge ki product_id duplicate hai ya nhi
            if product.product_id == myproduct.product_id:
                raise ValueError(f"Item '{myproduct.product_id}' already exists. Unable to create")# Agar same product ID milti hai to error
        mobilestoreRepo.add_product(product,product_name, product_quantity)# Agar product unique hai to database me add karenge
        # print(mobilestoreRepo.add_product(product_name, product_quantity))# Successfully add this statement in repo

    def update_product_quantity(self, product_id, quantity_to_add):#Quantity update krne k liye
        product_repo = ProductRepo()
        print(product_repo.update_quantity(product_id, quantity_to_add))

    def delete_product(self, product_id):
        mobilestoreRepo = ProductRepo()
        product_to_delete = product_id# Product khojenge
        for product in mobilestoreRepo.get_list():
            if product.product_id == product_id:
                product_to_delete = product
                break

        if product_to_delete is None:
            raise ValueError(f"Product with ID {product_id} not found")# Product nhi hai to product not found
        print(mobilestoreRepo.delete_product(product_id))
        # return f"Product with Product ID {product_id} has been deleted successfully"#Product hai to product delete

    def add_sale(self, sale, product_id, quantity_sold):  # Sale record karne ke liye
        product_repo = ProductRepo()
        print(product_repo.add_sale(sale, product_id, quantity_sold))

    def view_product(self, product_id):
        repo = ProductRepo()
        return(repo.view_product(product_id))