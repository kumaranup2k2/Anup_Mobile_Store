'''
Subject: Dukan (Dukan Main .exe file)
Created By: Anup Kumar
Created On: 29.Apr.2025
'''
import random
import pyodbc

def generate_unique_product_id():
    conn = pyodbc.connect(
        "DRIVER= driver;"
        "SERVER= server ;"
        "DATABASE= database name;"
        "UID= userid;"
        "PWD= password;"
    )
    cursor = conn.cursor()

    while True:
        product_id = random.randint(1000, 9999)  # 4-digit random ID
        cursor.execute("SELECT 1 FROM Anup_MOBILE_STORE WHERE product_id = ?", (product_id,))
        result = cursor.fetchone()
        if not result:
            cursor.close()
            conn.close()
            return product_id