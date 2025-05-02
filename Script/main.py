'''
Subject: Dukan (Dukan Main .exe file)
Created By: Anup Kumar
Created On: 29.Apr.2025
Modified On: 30.Apr.2025(Add More Function)
'''
from mobile_store.model.mobilemodel import mobilestore, sale
from mobile_store.service.productservice import ProductService
import time
import os
import platform
import id_generate

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    product_service = ProductService()

    try:
        # subprocess.run(["fastapi", "dev", "main.py"])
        while True:
            print(f"--- Anup Mobile Store Menu ---\n"
                  f"\n1. Add Product To Sale\n"
                  f"2. Delete Product\n"
                  f"3. Sales Product\n"
                  f"4. Product Detail\n"
                  f"5. Product Quantity Update\n"
                  f"6. Exit")
            user_input = input("Enter your choice (1-4): ")

            if user_input == "1":       #Add Product
                try:
                    seller_name = input("Enter Seller Name: ")
                    product_name = input("Enter Product Name: ")
                    product_quantity = int(input("Enter Product Quantity: "))
                    product_detail = input("Enter Product Detail: ")
                    product_price = float(input("Enter Product Price: "))
                    print("Your 4 digit Product Id Will Be Auto Generated....")
                    product_id = id_generate.generate_unique_product_id()
                    print("Your Product ID is: ",product_id)
                    new_product = mobilestore(
                        seller_name=seller_name,
                        product_name=product_name,
                        product_quantity=product_quantity,
                        product_detail=product_detail,
                        product_id = product_id,
                        product_price=product_price
                    )
                    product_service.add_product(new_product, product_name, product_quantity)
                except ValueError:
                    print("Please enter a valid Input!!! ")
                except Exception as e:
                    print("Error while adding product:", e)

            elif user_input == "2":     #Delete Product
                try:
                    product_id = int(input("Enter Product ID to delete: "))
                    product_service.delete_product(product_id)
                except ValueError:
                    print("Please enter a valid Input!!! ")
                except Exception as e:
                    print("Error while deleting product:", e)

            elif user_input == "3":     #Sale Product
                try:
                    product_id = int(input("Enter Product ID for Sale Product: "))
                    quantity_sold = int(input("Enter Quantity Sold: "))
                    new_sale = sale(
                        product_id=product_id,
                        quantity_sold=quantity_sold
                    )
                    product_service.add_sale(new_sale,product_id,quantity_sold)
                except ValueError:
                    print("Please enter a valid Input!!! ")
                except Exception as e:
                    print("Error while recording sale:", e)

            elif user_input == "4":     # Product Detail
                try:
                    product_id = int(input("Enter Product ID for Detail: "))
                    product = product_service.view_product(product_id)
                    if product:
                        print("Product Details------\n"
                              f"Product ID: {product[4]}\n"
                              f"Product Name: {product[1]}\n"
                              f"Seller Name: {product[0]}\n"
                              f"Quantity: {product[2]}\n"
                              f"Price: {product[5]}\n"
                              f"About Product: {product[3]}\n")
                    else:
                        print(f"No product found with ID {product_id}")
                except Exception as e:
                    print("Error fetching product detail:", e)

            elif user_input == "5":     # Update Product Quantity
                try:
                    product_id = int(input("Enter Product ID to update quantity: "))
                    quantity_to_add = int(input("Enter Quantity to Add: "))
                    result = product_service.update_product_quantity(product_id, quantity_to_add)
                except ValueError:
                    print("Please enter a valid Input!!! ")
                except Exception as e:
                    print("Error while updating product quantity:", e)

            elif user_input == "6":
                print("Thankyou... Have a Nice Day")
                time.sleep(3)
                break
            else:
                 print("Invalid Option Choose. Please choose 1-4.")
            input("Press Enter to continue...")
            clear_screen()
        pass

    except ValueError:
        print(" Character not Allowed Please enter a valid Option.")