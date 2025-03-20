# Generated: 2025-03-19 20:55:40.866751
# Result: [('East', 1, Decimal('42000.75')), ('North', 1, Decimal('50000.50'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate geographical sales dataset
conn.sql('''
CREATE TABLE sales (
    product VARCHAR,
    region VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO sales VALUES
('Laptop', 'North', 50000.50),
('Desktop', 'South', 35000.25),
('Tablet', 'East', 42000.75);
'''
)

# Demonstrate advanced group-by with HAVING clause
result = conn.sql('''
SELECT 
    region, 
    COUNT(*) as product_count,
    SUM(sales_amount) as total_sales
FROM sales
GROUP BY region
HAVING SUM(sales_amount) > 40000
''').fetchall()

print(result)