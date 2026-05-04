from config.connection import DatabaseConnection
from scripts.transform import transform
import pandas as pd

def load(df):
    db = DatabaseConnection()
    conn, cursor = db.connect()
    query = """
    INSERT INTO sales (
        transaction_id, transaction_date, customer_id, customer_name,
        region, category, product_name, quantity, unit_price,
        total_amount, payment_method, sales_rep, trans_status,
        discount, notes
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = df.values.tolist()

    cursor.executemany(query, data)
    conn.commit()

    db.close()
    return f"{len(data)} rows inserted successfully"