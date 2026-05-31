/* Total sales Revenue */
SELECT SUM(sale_amount) as total_revenue
from fact_sales;
/* Total Quantity sold */
SELECT SUM(quantity) as total_units_sold
from fact_sales;
/* Revenue by product category */
SELECT p.category,
    SUM(s.sale_amount) as total_revenue
FROM fact_Sales as s
    LEFT JOIN dim_product as p ON p.product_key = s.product_key
GROUP BY p.category
ORDER BY total_revenue DESC;
/* Top ten customers  */
SELECT c.customer_name,
    SUM(s.sale_amount) as amount_spent
FROM fact_sales as s
    LEFT JOIN dim_customer as c ON c.customer_key = s.customer_key
GROUP BY c.customer_id,
    c.customer_name
ORDER BY amount_spent DESC
LIMIT 10;
/* Monthly sales */
SELECT d.year,
    d.month_name,
    SUM(s.sale_amount) as monthly_revenue
FROM fact_sales as s
    LEFT JOIN dim_date as d ON d.date_key = s.date_key
GROUP BY d.year,
    d.month_name
ORDER BY monthly_revenue DESC;
/* Average trend */
SELECT ROUND(AVG(sale_amount), 2) avg_sale_value
FROM fact_sales;