CREATE TABLE IF NOT EXISTS fact_sales (
    sale_key INT PRIMARY KEY AUTO_INCREMENT,
    customer_key INT NOT NULL,
    product_key INT NOT NULL,
    date_key INT NOT NULL,
    quantity INT NOT NULL,
    sale_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
);
CREATE TABLE IF NOT EXISTS dim_customer (
    customer_key INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(100),
    effective_date DATE,
    expiry_date DATE,
    current_flag BOOLEAN DEFAULT TRUE,
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(50) DEFAULT 'ADMIN'
);
CREATE TABLE IF NOT EXISTS dim_product (
    product_key INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    product_name VARCHAR(255),
    category VARCHAR(100),
    price DECIMAL(10, 2),
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(50) DEFAULT 'ADMIN'
);
CREATE TABLE IF NOT EXISTS dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE,
    day_name VARCHAR(20),
    month_name VARCHAR(20),
    month INT,
    quarter INT,
    year INT
);