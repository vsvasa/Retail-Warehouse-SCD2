import pandas as pd
def get_dimension_table(table_name, conn):

    query = f"""
    SELECT *
    FROM {table_name}
    """

    return pd.read_sql(query, conn)

def create_fact_sales(sales_df, customer_dim, product_dim, date_dim):
    sales_df = pd.merge(sales_df, customer_dim[['customer_key','customer_id']], on='customer_id',how = 'left')
    sales_df = pd.merge(sales_df, product_dim[['product_key','product_id']], on='product_id',how = 'left')
    sales_df["date_key"] = (pd.to_datetime(sales_df["sale_date"]).dt.strftime("%Y%m%d").astype(int))
    fact_df = sales_df[['customer_key','product_key','date_key','quantity','sale_amount']]
    return fact_df