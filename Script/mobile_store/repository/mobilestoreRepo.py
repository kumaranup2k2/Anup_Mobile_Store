'''
Subject: Dukan (Mobile_store_Repository file)
Created By: Anup Kumar
Created On: 25.Apr.2025 (Add function)
Modified On: 27.Apr.2025 (Delete function)
Modified On: 29.Apr.2025 (Sale function,update_quantity)
Modified On: 30.Apr.2025(Solve Issues)
'''
import pyodbc
list_of_product = []

class ProductRepo ():
    def __init__(self):# database connection stablish
        try:
            self.conn = pyodbc.connect(
                "DRIVER= driver;"
                "SERVER= server ;"
                "DATABASE= database name;"
                "UID= userid;"
                "PWD= password;"
            )
            self.cursor = self.conn.cursor()
        except pyodbc.Error:
            print("Error while connecting to the database: Please Check Your Vpn is Connected or Not Connected")
            self.conn = None
            self.cursor = None

    def insert_data(self, query, data):#data insert
        try:
            if self.cursor:
                self.cursor.execute(query, data)
                self.conn.commit()  # Changes and save database
                return
        except pyodbc.Error as e:
            print("Error during data insertion:", e)
        finally:  # Kaam hone ke baad connection close
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()

    def get_list(self):
        return list_of_product

    def add_product(self, Anup_MOBILE_STORE, product_name, product_quantity):
        try:
            insert_query = 'INSERT INTO [Anup_MOBILE_STORE](' \
                           '[seller_name],' \
                           '[product_name],' \
                           '[product_quantity],' \
                           '[product_detail],' \
                           '[product_id],' \
                           '[product_price])' \
                           'VALUES (?, ?, ?, ?, ?, ?)'
            product_data = (Anup_MOBILE_STORE.seller_name,
                            Anup_MOBILE_STORE.product_name,
                            Anup_MOBILE_STORE.product_quantity,
                            Anup_MOBILE_STORE.product_detail,
                            Anup_MOBILE_STORE.product_id,
                            Anup_MOBILE_STORE.product_price)
            self.insert_data(insert_query, product_data)
            print(f"Product {product_name} Quentity {product_quantity} Added Successfully")
        except Exception as e:
            print("Error while adding the product:", e)

    def update_quantity(self, product_id, added_quantity):
        try:
            select_query = "SELECT product_quantity FROM [Anup_MOBILE_STORE] WHERE product_id = ?"
            self.cursor.execute(select_query, (product_id,))  # Get current quantity
            row = self.cursor.fetchone()
            if not row:
                return (f"Product with ID {product_id} not found.")
            current_quantity = row[0]
            new_quantity = current_quantity + added_quantity
            update_query = "UPDATE [Anup_MOBILE_STORE] SET product_quantity = ? WHERE product_id = ?"
            self.cursor.execute(update_query, (new_quantity, product_id))  # Add Quantity
            self.conn.commit()
            return (f"Product quantity Of Product ID {product_id} is Updated You can check on Product Detail")

        except pyodbc.Error as e:
            print("Error while updating product quantity:", e)

    def delete_product(self, product_id):
        try:
            delete_query = "DELETE FROM Anup_MOBILE_STORE WHERE product_id = ?"
            cursor = self.conn.cursor()
            cursor.execute(delete_query, (product_id,))
            self.conn.commit()
            if cursor.rowcount == 0:
                return (f"Product with ID {product_id} not found.")
            else:
                return (f"Product with Product ID {product_id} deleted successfully.")
        except pyodbc.Error as e:
            print("Error while deleting the product:", e)

    def add_sale(self, productsale, product_id, quantity_sold):
        try:
            product_check_query = "SELECT product_quantity FROM [Anup_MOBILE_STORE] WHERE Product_id = ?"
            self.cursor.execute(product_check_query, (productsale.product_id,))
            row = self.cursor.fetchone()# Product_id or product ka quantity check

            if not row:# Agar product nahi mila
                raise ValueError(f"Product with ID {productsale.product_id} does not exist.")

            current_quantity = row[0]
            if current_quantity == 0:
                return (f"Sorry This Stock Is Unavailable")
            elif current_quantity < productsale.quantity_sold:# Agar quantity kam hai
                return (f"Only {current_quantity} quantity available in stock.")
            else:
                update_query = "UPDATE [Anup_MOBILE_STORE] SET product_quantity = product_quantity - ? WHERE Product_id = ?"# Product ki quantity ko update
                self.cursor.execute(update_query, (productsale.quantity_sold, productsale.product_id))

                insert_sale_query = "INSERT INTO [productsale] (product_id, quantity_sold) VALUES (?, ?)"
                sale_data = (productsale.product_id, productsale.quantity_sold) #sale quantity update
                self.cursor.execute(insert_sale_query, sale_data)

                self.conn.commit()
                return (f"Product ID {product_id} Quentity {quantity_sold} Sale Successfully")

        except pyodbc.Error as e:
            print("Database error occurred:", e)
        except Exception as er:
            print("Unexpected error occurred:", er)

    def view_product(self, check_product_id):
        try:
            if self.conn and self.cursor:
                query = "SELECT * FROM Anup_MOBILE_STORE WHERE product_id = ?"
                self.cursor.execute(query, (check_product_id,))
                result = self.cursor.fetchone()
                if result :
                    return result
                else:
                    print (f"Product with ID {check_product_id} not found.")
        except pyodbc.Error as e:
            print("Database error:", e)
            return None