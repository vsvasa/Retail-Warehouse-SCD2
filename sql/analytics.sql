/* Top Customer by country*/
WITH customer_sale as (
    SELECT c.country,
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) as full_name,
        SUM(s.sale_amount) as amount_spent,
        ROW_NUMBER OVER(
            PARTITION by c.country
            ORDER BY SUM(s.sale_amount) DESC
        ) as rn
    FROM fact_sales as s
        LEFT JOIN dim_customer as c ON c.customer_key = s.customer_key
    GROUP BY c.country,
        c.customer_id,
        full_name
)
SELECT country,
    customer_id,
    full_name,
    amount_spent
FROM customer_sale
WHERE rn = 1;
/* Running Revenue*/
SELECT d.full_date,
    SUM(s.sale_amount) as daily_revenue,
    SUM(SUM(s.sale_amount)) OVER(
        ORDER BY d.full_date DESC
    ) as Running_Revenue
FROM fact_sales as s
    LEFT JOIN dim_date as d ON d.date_key = s.date_key
GROUP BY d.full_date
ORDER BY d.full_date DESC;
/* Business View */
CREATE OR REPLACE VIEW retail_sales as
SELECT s.sale_id,
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) as full_name,
    p.product_id,
    p.product_name,
    p.category,
    d.full_date,
    s.quantity,
    s.sale_amount
FROM fact_sales as s
    LEFT JOIN dim_customer as c ON c.customer_key = s.customer_key
    LEFT JOIN dim_product as p ON p.product_key = s.product_key
    LEFT JOIN dim_date as d ON d.date_key = s.date_key;
CREATE OR REPLACE VIEW Sales_Performance_v AS
SELECT d.year,
    d.month_name,
    p.category,
    COUNT(s.sale_id) as total_sales,
    SUM(s.quantity) as total_units_sold,
    SUM(s.sale_amount) as total_revenue
FROM fact_sales as s
    LEFT JOIN dim_product as p ON p.product_key = s.product_key
    LEFT JOIN dim_date as d ON d.date_key = s.date_key;