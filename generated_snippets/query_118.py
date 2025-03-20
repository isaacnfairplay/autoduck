# Generated: 2025-03-19 21:20:02.381491
# Result: [('Laptop', Decimal('1500.000'), datetime.date(2023, 2, 10), Decimal('2700.000'), 1), ('Laptop', Decimal('1200.000'), datetime.date(2023, 1, 15), Decimal('1200.000'), 2), ('Phone', Decimal('800.000'), datetime.date(2023, 1, 16), Decimal('800.000'), 3), ('Tablet', Decimal('500.000'), datetime.date(2023, 2, 15), Decimal('500.000'), 4)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample sales table with window functions
conn.execute('CREATE TABLE sales (product VARCHAR, amount DECIMAL, sale_date DATE)')
conn.execute("""INSERT INTO sales VALUES
    ('Laptop', 1200.00, '2023-01-15'),
    ('Phone', 800.00, '2023-01-16'),
    ('Laptop', 1500.00, '2023-02-10'),
    ('Tablet', 500.00, '2023-02-15')
""")

# Calculate running total and rank sales by amount
result = conn.execute("""
    SELECT 
        product, 
        amount, 
        sale_date,
        SUM(amount) OVER (PARTITION BY product ORDER BY sale_date) as running_total,
        RANK() OVER (ORDER BY amount DESC) as sales_rank
    FROM sales
""").fetchall()

print(result)