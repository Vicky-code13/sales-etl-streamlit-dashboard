CREATE TABLE IF NOT EXISTS sales (
    transaction_id VARCHAR(20) PRIMARY KEY,
    transaction_date DATE,
    customer_id VARCHAR(25) NOT NULL,
    customer_name VARCHAR(50),
    region VARCHAR(25),
    category VARCHAR(25),
    product_name VARCHAR(50),
    quantity INT,
    unit_price DECIMAL(10,2),
    total_amount DECIMAL(10,2),
    payment_method VARCHAR(20),
    sales_rep VARCHAR(50),
    trans_status VARCHAR(20),
    discount DECIMAL(5,2),
    notes TEXT
);