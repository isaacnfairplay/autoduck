# Generated: 2025-03-19 09:34:49.256872
# Result: [('Electronics', 'North', Decimal('3500.50'), 2), ('Electronics', 'South', Decimal('1200.75'), 1), ('Clothing', 'East', Decimal('800.25'), 1), ('Books', 'West', Decimal('450.00'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales dataset with multi-category analysis
conn.sql("""
CREATE TABLE sales (
    sale_id INTEGER,
    product_category VARCHAR,
    region VARCHAR,
    sale_amount DECIMAL(10,2),
    sale_date DATE
);

INSERT INTO sales VALUES
    (1, 'Electronics', 'North', 1500.50, '2023-01-15'),
    (2, 'Electronics', 'South', 1200.75, '2023-02-20'),
    (3, 'Clothing', 'East', 800.25, '2023-03-10'),
    (4, 'Books', 'West', 450.00, '2023-04-05'),
    (5, 'Electronics', 'North', 2000.00, '2023-05-12')
""");

# Analyze total sales by category and region
result = conn.sql("""
SELECT 
    product_category, 
    region, 
    SUM(sale_amount) as total_sales,
    COUNT(*) as sale_count
FROM sales
GROUP BY product_category, region
ORDER BY total_sales DESC
""").fetchall()

print(result)