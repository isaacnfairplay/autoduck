# Generated: 2025-03-19 20:53:48.864719
# Result: [('Desktop', 'South', 'Q1', Decimal('35000.00'), Decimal('35000.00')), ('Desktop', 'South', 'Q2', Decimal('41000.00'), Decimal('76000.00')), ('Laptop', 'North', 'Q1', Decimal('50000.00'), Decimal('50000.00')), ('Laptop', 'North', 'Q2', Decimal('62000.00'), Decimal('112000.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with multiple dimensions
conn.sql("""
CREATE TABLE sales (
    product VARCHAR,
    region VARCHAR,
    quarter VARCHAR,
    revenue DECIMAL(10, 2)
);

INSERT INTO sales VALUES
('Laptop', 'North', 'Q1', 50000.00),
('Desktop', 'South', 'Q1', 35000.00),
('Laptop', 'North', 'Q2', 62000.00),
('Desktop', 'South', 'Q2', 41000.00);
""")

# Use window function to calculate cumulative revenue per region
result = conn.sql("""
SELECT 
    product, 
    region, 
    quarter, 
    revenue,
    SUM(revenue) OVER (PARTITION BY region ORDER BY quarter) as cumulative_revenue
FROM sales
""").fetchall()

print(result)