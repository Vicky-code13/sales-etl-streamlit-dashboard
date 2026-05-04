import pandas as pd
import numpy as np


def extract_data():
    df = pd.read_excel('data/ETL_Sales_Dataset.xlsx') 
    df = df.rename(columns={"Transaction_ID": "transaction_id", "Date": "transaction_date", "Customer_ID": "customer_id", "Customer_Name": "customer_name", 
                       "Region": "region", "Category":"category", "Product_Name": "product_name", "Quantity": "quantity", 
                       "Unit_Price": "unit_price", "Total_Amount": "total_amount", "Payment_Method": "payment_method", "Sales_Rep": "sales_rep", 
                       "Status": "trans_status", "Discount_%": "discount", "Notes": "notes"})

    return df