from utils import setup_logger,create_connection
from extract import extract_csv
from date_dimension  import generate_date_dimension
from dimension_loader import load_dimension
from fact_loader import create_fact_sales,get_dimension_table
import pandas as pd
logger = setup_logger()

def main():
    
    try:
        conn = create_connection()

        if not conn:
            logger.error("Failed to connect to database")
            return
        else:
            logger.info(f"{conn.database} connected to the database successfully")
        
        # extract customers CSV
        customers_df = extract_csv("data/raw/customers.csv",["customer_id","first_name","last_name","email","city","state","country"])
        logger.info(f"Extracted {len(customers_df)} records from customers.csv")
        load_dimension(customers_df,"dim_customer",conn)
        logger.info(f"Loaded {len(customers_df)} records into dim_customer")

        # extract products csv

        products_df = extract_csv("data/raw/products.csv",["product_id","product_name","category","price"])
        products_df["product_name"] = (
            products_df["product_name"]
            .fillna("Unknown Product")
        )

        logger.info(f"Extracted {len(products_df)} records from products.csv")
        load_dimension(products_df,"dim_product",conn)
        logger.info(f"Loaded {len(products_df)} records into dim_product")

        # load date dimension 

        date_df = generate_date_dimension()
        load_dimension(date_df,"dim_date",conn)
        logger.info(f"Loaded {len(date_df)} records into dim_date")

        # Extracting sales data
        sales_df = extract_csv("data/raw/sales.csv",["sale_id","customer_id","product_id","sale_date","quantity","sale_amount"])
        sales_df["sale_date"] = pd.to_datetime(sales_df["sale_date"])
        
        customer_dim = get_dimension_table("dim_customer", conn)
        product_dim = get_dimension_table("dim_product", conn)
        date_dim = get_dimension_table("dim_date", conn)

        logger.info("Customer dimension:", customer_dim.head())
        logger.info("Product dimension:", product_dim.head())
        logger.info("Date dimension:", date_dim.head())
        fact_sales_df = create_fact_sales(sales_df,customer_dim,product_dim,date_dim)
        logger.info("Fact sales:", fact_sales_df.head())
        
        
        logger.info("loading sales data to the database")
        load_dimension(fact_sales_df,"fact_sales",conn)
        logger.info("loaded sales data to the database successfully")

        
        conn.close()
        logger.info("Warehouse dimension loaded successfully")

    except Exception as e:
        logger.error(f"Error loading warehouse dimension: {e}")

if __name__ == "__main__":
    main()
        