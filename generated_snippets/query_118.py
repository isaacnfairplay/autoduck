# Generated: 2025-03-19 11:11:48.366343
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create two tables for UNION ALL demonstration
conn.execute('''
CREATE TABLE sales_2022 (product VARCHAR, revenue DECIMAL(10,2));
CREATE TABLE sales_2023 (product VARCHAR, revenue DECIMAL(10,2));

INSERT INTO sales_2022 VALUES
    ('Laptop', 500000.00),
    ('Smartphone', 350000.00);

INSERT INTO sales_2023 VALUES
    ('Laptop', 600000.00),
    ('Tablet', 250000.00);

-- Combine sales data from two years using UNION ALL
SELECT product, revenue, '2022' as year FROM sales_2022
UNION ALL
SELECT product, revenue, '2023' as year FROM sales_2023;
''').fetchall()