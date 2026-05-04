import streamlit as st
import pandas as pd
import mysql.connector

# connect DB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin@123",
    database="etl"
)

query = "SELECT * FROM sales"
df = pd.read_sql(query, conn)

st.title("Sales Dashboard")

# KPI
st.metric("Total Revenue", int(df["total_amount"].sum()))

# chart
st.subheader("Sales by Categories")
category = df.groupby("category")["total_amount"].sum()
st.bar_chart(category)

# trend
st.subheader("Sales Trend")
df["transaction_date"] = pd.to_datetime(df["transaction_date"])
trend = df.groupby("transaction_date")["total_amount"].sum()
st.line_chart(trend)