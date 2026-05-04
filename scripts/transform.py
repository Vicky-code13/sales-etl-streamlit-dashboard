import pandas as pd
import numpy as np


def transform(df):
    null_cols = df.isnull().sum()  # For checking null values

    df = df.dropna(subset=["customer_id"])
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], format="mixed").dt.date
    df["notes"] = df["notes"].fillna('NULL')

    # Case 1: missing quantity
    df.loc[df["quantity"].isnull() & df["unit_price"].notnull(), "quantity"] = (df["total_amount"] // df["unit_price"])

    # Case 2: missing unit price
    df.loc[df["unit_price"].isnull() & df["quantity"].notnull(), "unit_price"] = (df["total_amount"] / df["quantity"])

    af_null_cols = df.isnull().sum()  # For checking null values
    return df