# Generated: 2025-03-16 22:48:56.847310
# Result: [(1, datetime.date(2023, 1, 15), 10, Decimal('500.00'), Decimal('500.00'), 12.5), (1, datetime.date(2023, 2, 20), 15, Decimal('750.00'), Decimal('1250.00'), 12.5), (2, datetime.date(2023, 1, 10), 5, Decimal('250.00'), Decimal('250.00'), 6.5), (2, datetime.date(2023, 2, 25), 8, Decimal('400.00'), Decimal('650.00'), 6.5)]
# Valid: True
import duckdb

# Establish in-memory database connection
conn = duckdb.connect(':memory:')

# Create sample sales data table
conn.execute('''
CREATE TABLE sales (
    product_id INT,
    sale_date DATE,
    quantity INT,
    total_revenue DECIMAL(10,2)
);

INSERT INTO sales VALUES
    (1, '2023-01-15', 10, 500.00),
    (1, '2023-02-20', 15, 750.00),
    (2, '2023-01-10', 5, 250.00),
    (2, '2023-02-25', 8, 400.00);
''')

# Advanced window function query
result = conn.execute('''
SELECT 
    product_id,
    sale_date,
    quantity,
    total_revenue,
    SUM(total_revenue) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_revenue,
    AVG(quantity) OVER (PARTITION BY product_id) as avg_product_quantity
FROM sales
ORDER BY product_id, sale_date
''').fetchall()

print(result)