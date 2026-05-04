from database.setup_db import schema_creation
from scripts.extract import extract_data
from scripts.transform import transform
from scripts.load import load
import pandas as pd

def run_pipeline():
    schema_creation()
    df = extract_data()
    df = transform(df)
    df = df.where(pd.notnull(df), None)
    load(df)



if __name__ == "__main__":
    run_pipeline()