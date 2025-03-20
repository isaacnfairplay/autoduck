# Generated: 2025-03-19 20:57:23.134306
# Result: [('USA', 'Laptop', Decimal('50000.50'), 1, 1), ('Japan', 'Tablet', Decimal('42000.75'), 2, 2), ('Germany', 'Desktop', Decimal('35000.25'), 3, 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create custom table with geographic sales data
conn.sql('''
CREATE TABLE world_sales (
    country VARCHAR,
    product VARCHAR,
    sales_amount DECIMAL(10,2),
    sales_quarter VARCHAR
);

INSERT INTO world_sales VALUES
('USA', 'Laptop', 50000.50, 'Q1'),
('Germany', 'Desktop', 35000.25, 'Q2'),
('Japan', 'Tablet', 42000.75, 'Q1');
''')

# Demonstrate advanced window function with rank and dense_rank
result = conn.sql('''
SELECT
    country,
    product,
    sales_amount,
    RANK() OVER (ORDER BY sales_amount DESC) as sales_rank,
    DENSE_RANK() OVER (ORDER BY sales_amount DESC) as dense_sales_rank
FROM world_sales
''').fetchall()

print(result)